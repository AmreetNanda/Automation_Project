import os
import time
from ai.ollama_client import ask_ollama
from ai.prompts import TEST_GENERATION_PROMPT

def generate_test(user_request: str) -> str:
    # Directly replace placeholder without using .format()
    prompt = TEST_GENERATION_PROMPT.replace("{user_request}", user_request)

    try:
        code = ask_ollama(prompt)
    except Exception as e:
        raise RuntimeError(f"AI generation failed: {e}")

    if not code or not code.strip():
        raise RuntimeError("Generated test code is empty")

    # Check forbidden patterns
    FORBIDDEN = [
        "webdriver.Remote",
        "desired_caps",
        "from selenium.webdriver",
        "By.",
        "driver = create_driver()",
        "from appium.webdriver.common.by import By",
    ]
    for bad in FORBIDDEN:
        if bad in code:
            raise RuntimeError(f"AI generated forbidden pattern: {bad}")

    # Check required patterns
    REQUIRED = [
        "from appium.webdriver.common.appiumby import AppiumBy",
        "driver.activate_app",
        "save_screenshot",
        "pytest.fail",
        "logging"
    ]
    for need in REQUIRED:
        if need not in code:
            raise RuntimeError(f"AI missing required pattern: {need}")

    # Save generated test
    os.makedirs("tests", exist_ok=True)
    filename = f"test_ai_{int(time.time())}.py"
    path = os.path.join("tests", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    return path
