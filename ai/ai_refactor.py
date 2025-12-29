import re

def refactor_ai_code(code: str) -> str:
    # Remove class definitions
    code = re.sub(r"class\s+Test.*?:", "", code)

    # Remove setup/teardown
    code = re.sub(r"def setup_method.*?:[\s\S]*?def", "def", code)
    code = re.sub(r"def teardown_method.*?:[\s\S]*?\n", "", code)

    # Replace Selenium By with AppiumBy
    code = code.replace(
        "from appium.webdriver.common.by import By",
        "from appium.webdriver.common.appiumby import AppiumBy"
    )

    # Replace deprecated find_element_by
    code = re.sub(
        r"find_element_by\((.*?)\)",
        r"find_element(AppiumBy.ACCESSIBILITY_ID, \1)",
        code
    )

    return code
