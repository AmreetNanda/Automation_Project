import json
from ml.data.schemas import TestExecutionSample

def collect(sample: TestExecutionSample):
    with open("ml/data/raw/executions.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(sample.__dict__) + "\n")
