from ml.data.locator_dataset import load_locator_stats
from ml.models.locator_reliability import LocatorReliabilityModel

def main():
    X, y, _ = load_locator_stats()

    model = LocatorReliabilityModel()
    model.train(X, y)
    model.save()

    print("✅ Locator reliability model trained.")

if __name__ == "__main__":
    main()
