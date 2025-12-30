from selenium.common.exceptions import NoSuchElementException
from utils.locator_logger import log_locator_event

def safe_find(driver, test_name, by, value, screen=None):
    try:
        el = driver.find_element(by, value)
        log_locator_event(test_name, by, value, True, screen)
        return el
    except NoSuchElementException:
        log_locator_event(test_name, by, value, False, screen)
        raise
