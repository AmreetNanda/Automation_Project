import json
import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "healing_events.json")

def log_healing_event(failed_locator, new_locator, success):
    """Save each self-healing attempt for later ML analysis."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    event = {
        "timestamp": datetime.now().isoformat(),
        "failed_locator": failed_locator,
        "new_locator": new_locator,
        "success": success
    }
    
    # Append event to file
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(event)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
