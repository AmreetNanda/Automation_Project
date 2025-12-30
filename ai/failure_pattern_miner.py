import json
from collections import Counter

def mine_common_failures(path="data/healing_events.jsonl"):
    counter = Counter()
    with open(path) as f:
        for line in f:
            event = json.loads(line)
            counter[event["failed_locator"]] += 1
    return counter.most_common(10)
