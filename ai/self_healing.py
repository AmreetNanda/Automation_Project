from ai.ollama_client import ask_ollama

def heal_locator(failed_locator, page_source):
    prompt = f"""
    A locator failed in Appium.

    Failed locator:
    {failed_locator}

    Page source:
    {page_source[:5000]}

    Suggest a better locator strategy (ID, accessibility_id, xpath).
    """
    return ask_ollama(prompt)
