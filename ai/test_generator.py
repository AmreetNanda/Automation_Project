import os
import time
from ai.ollama_client import ask_ollama
from ai.prompts import TEST_GENERATION_PROMPT
from ai.code_normalizer import normalize_appiumby
from ai.code_sanitizer import strip_code_fences

# Forbidden and required patterns
FORBIDDEN = [
    "webdriver.Remote",
    "desired_caps",
    "from selenium.webdriver",
    "By.",
    "driver = create_driver()",
    "AppiumAppium",
    "AppiumACCESSIBILITY",
    "ACCESSIBILITY_Appium",
    "```",
    "```python",
]

REQUIRED = [
    "from appium.webdriver.common.appiumby import AppiumBy",
    "driver.activate_app",
    "save_screenshot",
    "pytest.fail",
    "logging"
]

MAX_RETRIES = 3

def generate_test(user_request: str, log_callback=None) -> str:
    prompt = TEST_GENERATION_PROMPT.replace("{user_request}", user_request)
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            if log_callback:
                log_callback(f"AI Generation Attempt {attempt}...\n")
            
            code = ask_ollama(prompt)
            code = strip_code_fences(code)
            code = normalize_appiumby(code)
            
            if log_callback:
                log_callback("Raw AI output:\n" + code + "\n")
            
            # Auto-clean forbidden patterns
            for bad in FORBIDDEN:
                if bad in code:
                    code = code.replace(bad, "")
                    if log_callback:
                        log_callback(f"Removed forbidden pattern: {bad}\n")
            
            # Check required patterns
            missing = [need for need in REQUIRED if need not in code]
            if missing:
                if log_callback:
                    log_callback(f"Missing required patterns: {missing}\n")
                raise RuntimeError(f"AI missing required pattern(s): {', '.join(missing)}")
            
            # Save the cleaned, verified code
            os.makedirs("tests", exist_ok=True)
            filename = f"test_ai_{int(time.time())}.py"
            path = os.path.join("tests", filename)
            with open(path, "w", encoding="utf-8") as f:
                f.write(code)
            
            if log_callback:
                log_callback(f"Test saved: {path}\n")
            
            return path
        
        except Exception as e:
            if log_callback:
                log_callback(f"Attempt {attempt} failed: {e}\n")
            time.sleep(1)  # Small delay before retry
    
    raise RuntimeError(f"AI test generation failed after {MAX_RETRIES} attempts. See AI logs for details.")
