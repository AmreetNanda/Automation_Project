TEST_GENERATION_PROMPT = """
You are an expert Appium + Pytest automation engineer. Follow these rules **exactly**:

MANDATORY RULES:
- NEVER create a WebDriver or desired capabilities.
- NEVER import anything from selenium.webdriver.
- NEVER use `By`.
- ALWAYS use `AppiumBy` for locating elements.
- ALWAYS use the pytest fixture named `driver`; do NOT create or assign the driver inside the test.
- ALWAYS wrap all test actions in try/except.
- ALWAYS take screenshots on failure into the 'screenshot' directory.
- ALWAYS call pytest.fail(...) on failure.
- ALWAYS log all actions using `logging`.
- NO comments outside code, NO markdown, NO explanations.
- DO NOT generate any code that matches these forbidden patterns:
    "webdriver.Remote", "desired_caps", "from selenium.webdriver", "By.", "driver = create_driver()", "webdriver"

REFERENCE TEST STYLE:

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
    try:
        driver.find_element(AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_text_box")
        return True
    except NoSuchElementException:
        return False
    
def open_maps(driver):
    if not is_maps_open(driver):
        logging.info("Opening Google Maps")
        driver.activate_app("com.google.android.apps.maps")
        time.sleep(3)
    else:
        logging.info("Google Maps already open")

def click_coffee_shop_button(driver):
    try:
        coffee_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Coffee shops")
        coffee_button.click()
        logging.info("Clicked Coffee Shops button")
    except NoSuchElementException:
        screenshot_path = os.path.join(SCREENSHOT_DIR, "coffee_button_not_found.png")
        driver.save_screenshot(screenshot_path)
        logging.info("Coffee shop button not found. Screenshot saved")
        raise Exception(f"Coffee shop button not found. Screenshot saved at {screenshot_path}")

@pytest.fixture
def driver():
    driver_instance = create_driver()
    yield driver_instance
    quit_driver(driver_instance)

TASK:
Generate a new pytest test following **exactly** the same style and structure above
for the following description:

{user_request}

Return ONLY valid Python code, fully compatible with the framework above,
using the driver fixture, AppiumBy, logging, and screenshots.
Do NOT create a driver inside the test.
Do NOT import forbidden modules.
Do NOT include forbidden patterns.
"""
