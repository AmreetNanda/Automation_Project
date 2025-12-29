from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"

driver = webdriver.Remote("http://localhost:4723", options=options)
print(driver.session_id)  # should print a valid session id
driver.quit()
