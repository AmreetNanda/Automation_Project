import re

def normalize_appiumby(code: str) -> str:
    replacements = {
        r"\bAppiumAppiumID\b": "AppiumBy.ID",
        r"\bAppiumID\b": "AppiumBy.ID",
        r"\bAppiumACCESSIBILITY_ID\b": "AppiumBy.ACCESSIBILITY_ID",
        r"\bAppiumAppiumACCESSIBILITY_AppiumID\b": "AppiumBy.ACCESSIBILITY_ID",
        r"\bACCESSIBILITY_ID\b": "AppiumBy.ACCESSIBILITY_ID",
    }

    for pattern, replacement in replacements.items():
        code = re.sub(pattern, replacement, code)

    # Ensure driver setup import lines are present
    if "from utils.driver_setup import create_driver, quit_driver" not in code:
        code = "from utils.driver_setup import create_driver, quit_driver\n" + code

    if 'SCREENSHOT_DIR = "screenshot"' not in code:
        code = 'SCREENSHOT_DIR = "screenshot"\nos.makedirs(SCREENSHOT_DIR, exist_ok=True)\n' + code

    return code
