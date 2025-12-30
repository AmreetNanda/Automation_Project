import json
from collections import defaultdict

def load_locator_stats(path="ml/data/raw/locator_events.jsonl"):
    stats = defaultdict(lambda: {"success": 0, "fail": 0})

    with open(path, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            key = (r["locator_type"], r["locator_value"])
            if r["success"]:
                stats[key]["success"] += 1
            else:
                stats[key]["fail"] += 1

    X, y = [], []

    for (lt, lv), s in stats.items():
        total = s["success"] + s["fail"]
        success_rate = s["success"] / total if total else 0

        X.append([
            1 if lt == "id" else 0,
            1 if lt == "accessibility id" else 0,
            1 if lt == "xpath" else 0,
            success_rate,
            total,
        ])

        y.append(success_rate)

    return X, y, stats
