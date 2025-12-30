import re
from ai.ollama_client import ask_ollama
from ai.healing_logger import log_healing_event
import json
from datetime import datetime

# def heal_locator(failed_locator, page_source):
#     prompt = f"""
#     You are an Appium automation expert.

#     A locator failed:
#     {failed_locator}

#     Page source (truncated):
#     {page_source[:4000]}

#     Return ONLY one valid Python locator in this format:
#     AppiumBy.ID, "value"
#     OR
#     AppiumBy.ACCESSIBILITY_ID, "value"
#     OR
#     AppiumBy.XPATH, "value"
#     """

#     response = ask_ollama(prompt)

#     match = re.search(
#         r"(AppiumBy\.\w+)\s*,\s*[\"'](.+?)[\"']",
#         response
#     )

#     if not match:
#         return None

#     return {
#         "by": match.group(1),
#         "value": match.group(2)
#     }

# def log_healing_event(failed, healed, success):
#     record = {
#         "timestamp": datetime.utcnow().isoformat(),
#         "failed_locator": failed,
#         "healed_locator": healed,
#         "success": success
#     }
#     with open("data/healing_events.jsonl", "a") as f:
#         f.write(json.dumps(record) + "\n")



def heal_locator(failed_locator, page_source, test_runner=None):
    prompt = f"""
    A locator failed in Appium.

    Failed locator:
    {failed_locator}

    Page source:
    {page_source[:5000]}

    Suggest a better locator strategy (ID, accessibility_id, xpath).
    """
    new_locator = ask_ollama(prompt)

    # If you have a test_runner, attempt to verify success (optional)
    success = False
    if test_runner:
        try:
            # Example: test_runner.click(new_locator)
            # success = True if no exception
            success = True  # Placeholder; integrate real retry logic
        except Exception:
            success = False

    log_healing_event(failed_locator, new_locator, success)
    return new_locator
