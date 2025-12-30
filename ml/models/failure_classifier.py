from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

class FailureClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=50)
        self.encoder = LabelEncoder()

    def train(self, X, y):
        y_encoded = self.encoder.fit_transform(y)
        self.model.fit(X, y_encoded)

    def predict(self, X):
        preds = self.model.predict(X)
        return self.encoder.inverse_transform(preds)

    def save(self, path="ml/models/failure_model.pkl"):
        joblib.dump((self.model, self.encoder), path)

    def load(self, path="ml/models/failure_model.pkl"):
        self.model, self.encoder = joblib.load(path)
