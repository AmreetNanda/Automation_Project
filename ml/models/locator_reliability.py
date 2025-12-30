from sklearn.linear_model import LinearRegression
import joblib

class LocatorReliabilityModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path="ml/models/locator_model.pkl"):
        joblib.dump(self.model, path)

    def load(self, path="ml/models/locator_model.pkl"):
        self.model = joblib.load(path)
