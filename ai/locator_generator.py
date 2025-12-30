from appium.webdriver.common.appiumby import AppiumBy

def generate_locator_candidates(original):
    value = original["value"]

    candidates = [
        (AppiumBy.ID, value),
        (AppiumBy.ACCESSIBILITY_ID, value),
        (AppiumBy.XPATH, f"//*[@text='{value}']"),
        (AppiumBy.XPATH, f"//*[contains(@text,'{value.split()[0]}')]"),
    ]

    return candidates
