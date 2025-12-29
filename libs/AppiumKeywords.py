import yaml
from appium import webdriver
import time


class AppiumKeywords:

    def __init__(self):
        self.driver = None

    def load_capabilities(self, config_path="config/capabilities.yaml", profile="AAOS"):
        with open(config_path, "r") as file:
            caps = yaml.safe_load(file)
        return caps[profile]

    def start_aaos_session(self):
        caps = self.load_capabilities()
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        time.sleep(5)
        return self.driver

    def click_element_by_id(self, element_id):
        self.driver.find_element("id", element_id).click()

    def input_text_by_id(self, element_id, text):
        element = self.driver.find_element("id", element_id)
        element.clear()
        element.send_keys(text)

    def element_should_be_visible(self, element_id):
        element = self.driver.find_element("id", element_id)
        if not element.is_displayed():
            raise AssertionError(f"Element {element_id} is not visible")

    def stop_session(self):
        if self.driver:
            self.driver.quit()
