from ai.ollama_client import ask_ollama
from ml.data.collector import collect
from ml.data.schemas import TestExecutionSample

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
