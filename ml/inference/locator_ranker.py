from ml.models.locator_reliability import LocatorReliabilityModel

def encode(locator):
    by, value = locator
    return [
        1 if by.endswith("ID") else 0,
        1 if by.endswith("ACCESSIBILITY_ID") else 0,
        1 if by.endswith("XPATH") else 0,
        0.5,  # placeholder reliability prior
        len(value)
    ]

def rank_locators(candidates):
    model = LocatorReliabilityModel()
    model.load()

    scored = []
    for c in candidates:
        score = model.predict([encode(c)])[0]
        scored.append((score, c))

    return sorted(scored, reverse=True)
