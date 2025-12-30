import json
import time

LOG_FILE = "ml/data/raw/locator_events.jsonl"

def log_locator_event(
    test_name: str,
    locator_type: str,
    locator_value: str,
    success: bool,
    screen: str = None
):
    record = {
        "timestamp": time.time(),
        "test_name": test_name,
        "locator_type": locator_type,
        "locator_value": locator_value,
        "success": success,
        "screen": screen,
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
