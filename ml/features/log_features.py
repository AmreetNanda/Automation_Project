import re

def extract_features(pytest_log: str, appium_log: str) -> dict:
    text = (pytest_log + " " + appium_log).lower()

    return {
        "has_no_such_element": int("nosuchelementexception" in text),
        "has_timeout": int("timeout" in text),
        "has_permission": int("permission" in text),
        "has_app_crash": int("crash" in text or "not launched" in text),
        "log_length": len(text),
    }
