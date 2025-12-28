from appium import webdriver
from config.capabilities import get_android_options
import time

def create_driver():
    options = get_android_options()
    server_url = "http://localhost:4723"  
    driver = webdriver.Remote(command_executor=server_url, options=options)
    time.sleep(2)  # wait for app to launch
    return driver

def quit_driver(driver):
    if driver:
        driver.quit()
