import re
from ai.ollama_client import ask_ollama
from ai.ollama_client import ask_ollama

def heal_locator(failed_locator, page_source):
    prompt = f"""
    You are an Appium automation expert.

    A locator failed:
    {failed_locator}

    Page source (truncated):
    {page_source[:4000]}

    Return ONLY one valid Python locator in this format:
    AppiumBy.ID, "value"
    OR
    AppiumBy.ACCESSIBILITY_ID, "value"
    OR
    AppiumBy.XPATH, "value"
    """

    response = ask_ollama(prompt)

    match = re.search(
        r"(AppiumBy\.\w+)\s*,\s*[\"'](.+?)[\"']",
        response
    )

    if not match:
        return None

    return {
        "by": match.group(1),
        "value": match.group(2)
    }
