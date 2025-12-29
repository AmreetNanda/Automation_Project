import time
import os
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from logger import logging
import sys
from exception import CustomException

from utils.driver_setup import create_driver, quit_driver

SCREENSHOT_DIR = "screenshot"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def is_maps_open(driver) -> bool:
    """Checks if Google maps is currently in the foreground"""
    try:
        driver.find_element(AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_text_box")
        return True
    except NoSuchElementException:
        return False
    
def open_maps(driver):
    """Launch google maps if not already open"""
    if not is_maps_open(driver):
        print("Maps not open -> Launching google maps ... ")
        logging.info("Opening maps now")
        driver.activate_app("com.google.android.apps.maps")
        logging.info("Google maps is now opened")
        time.sleep(3)
    else:
        print("Google maps is already open")
        logging.info("Google maps is already open")


def click_coffee_shop_button(driver):
    """Tap the coffee shop category button."""
    try:
        coffee_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Coffee shops")
        coffee_button.click()
        print("Clicked 'coffee shops' button successfully. ")
        logging.info("Clicked 'Coffee Shops' button successfullly. ")
    except NoSuchElementException:
        screenshot_path = os.path.join(SCREENSHOT_DIR, "coffee_button_not_found.png")
        driver.save_screenshot(screenshot_path)
        logging.info("Coffee shop button not found. Screenshot saved")
        raise Exception(f"Coffee shop button not found. Screenshot saved at {screenshot_path}")

def test_open_maps_and_click_coffee(driver):
    """Test to open Maps and click Coffee shop button."""
    try:
        time.sleep(3)
        open_maps(driver)
        logging.info("Tapping on Coffee button")
        click_coffee_shop_button(driver)
        logging.info("Coffee button is now open")
        time.sleep(3)
        # Close Google maps and return to Home
        driver.terminate_app("com.google.android.apps.maps")
        logging.info("Pressing Home button")
        driver.press_keycode(3)  # HOME button
        logging.info("Returned to Home screen")
    except Exception as e:
        # Take screenshot on failure
        screenshot_path = os.path.join(SCREENSHOT_DIR, "test_failure.png")
        driver.save_screenshot(screenshot_path)
        logging.info("Test case failed. Check the screenshot")
        pytest.fail(f"Test failed: {e}. Screenshot saved at {screenshot_path}")
        raise CustomException(e, sys)

# from utils.element_finder import find_element_with_healing
# def click_coffee_shop_button(driver):
#     try:
#         coffee_button = find_element_with_healing(
#             driver,
#             AppiumBy.ACCESSIBILITY_ID,
#             "Coffee shops",
#             description="Coffee shop button"
#         )
#         coffee_button.click()
#         logging.info("Clicked Coffee Shops button")

#     except NoSuchElementException:
#         screenshot_path = os.path.join(SCREENSHOT_DIR, "coffee_button_not_found.png")
#         driver.save_screenshot(screenshot_path)
#         raise Exception("Coffee shop button not found")

@pytest.fixture
def driver():
    driver_instance = create_driver()
    yield driver_instance
    quit_driver(driver_instance)