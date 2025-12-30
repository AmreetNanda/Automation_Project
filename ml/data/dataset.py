import json
from ml.features.log_features import extract_features
from ml.models.labels import FailureType

def load_dataset(path="ml/data/raw/executions.jsonl"):
    X, y = [], []

    with open(path, encoding="utf-8") as f:
        for line in f:
            record = json.loads(line)

            features = extract_features(
                record["pytest_log"],
                record["appium_log"]
            )

            label = record.get("failure_reason", FailureType.UNKNOWN)
            X.append(list(features.values()))
            y.append(label)

    return X, y
