import time
import os
import pytest
from math import sqrt
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from utils.driver_setup import create_driver, quit_driver
from logger import logging

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture
def driver():
    instance = create_driver()
    yield instance
    quit_driver(instance)

def is_map_open(driver) -> bool:
    try:
        driver.find_element(AppiumBy.ID, "com.google.android.apps.maps:id/main_suggested_destinations_search_box")
        return True
    except NoSuchElementException:
        return False

def open_maps(driver):
    if not is_map_open(driver):
        logging.info("Opening maps now")
        driver.activate_app("com.google.android.apps.maps")
        logging.info("Google maps is now opened")
        time.sleep(3)

def click_search_bar(driver):
    el = driver.find_element(AppiumBy.ID, "com.google.android.apps.maps:id/main_suggested_destinations_search_box")
    el.click()
    time.sleep(1)

def enter_location_search(driver, location):
    input_field = driver.find_element(AppiumBy.ID, "com.google.android.apps.maps:id/destination_input_keyword_search_edit_text")
    input_field.click()
    input_field.send_keys(location)
    time.sleep(2)

def select_first_option(driver):
    option = driver.find_element(AppiumBy.XPATH, "//*[@text='HSR Layout']/parent::android.widget.FrameLayout")
    option.click()
    time.sleep(2)

def click_start_navigation(driver):
    start_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Start")
    start_btn.click()
    time.sleep(4)

def test_route_to_hsr_with_gps_simulation(driver):
    """
    1. Open maps 
    2. Search HSR Layout
    3. Select first result
    4. Start Navigation
    """
    try:
        open_maps(driver)
        click_search_bar(driver)
        enter_location_search(driver)
        select_first_option(driver)
        click_start_navigation(driver)

        start_point = "Your Current Location"
        end_point = "HSR Layout, Bengaluru"

        driver.terminate_app("com.google.android.apps.maps")
        driver.press_keycode(3) # Home button
        logging.info("Returned to home screen")
    except Exception as e:
        screenshot = os.path.join(SCREENSHOT_DIR, "failure_gps_sim.png")
        driver.save_screenshot(screenshot)
        pytest.fail(f"Test failed: {e}. screenshot saved at: {screenshot}")
