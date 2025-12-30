from ai.ollama_client import ask_ollama
from ml.data.collector import collect
from ml.data.schemas import TestExecutionSample
import re

def analyze_failure(pytest_log, appium_log):
    prompt = f"""
    Analyze this Appium test failure.

    Pytest Log:
    {pytest_log}

    Appium Log:
    {appium_log}

    Provide:
    - Root cause
    - Fix suggestion
    - Locator or timing issues
    """
    return ask_ollama(prompt)

LOCATOR_PATTERNS = [
    r"find_element\((.*?),\s*['\"](.*?)['\"]\)",
]

def extract_failed_locator(pytest_log: str):
    for pattern in LOCATOR_PATTERNS:
        match = re.search(pattern, pytest_log)
        if match:
            return {
                "by": match.group(1),
                "value": match.group(2)
            }
    return None
