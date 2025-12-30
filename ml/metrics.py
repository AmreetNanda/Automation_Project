def healing_success_rate(events):
    total = len(events)
    success = sum(1 for e in events if e["success"])
    return success / max(total, 1)
