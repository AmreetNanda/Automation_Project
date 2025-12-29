from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from logger import logging
from ai.self_healing import heal_locator

def find_element_with_healing(driver, by, value, description=""):
    try:
        return driver.find_element(by, value)

    except NoSuchElementException:
        logging.error(f"Locator failed: {by}={value} ({description})")

        # 🔧 AI Self-Healing
        healed_locator = heal_locator(
            failed_locator=f"{by}={value}",
            page_source=driver.page_source
        )

        logging.info(f"🤖 AI Suggested Locator: {healed_locator}")

        # Fail fast (do NOT auto-execute unknown locators yet)
        raise
