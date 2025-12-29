TEST_CASES = {
    "Google Maps - Coffee Shop Test": "tests/test_coffee_maps.py",
    "Google Maps - Check Route Navigation": "tests/test_route_navigation.py",
}

def list_test_cases():
    return list(TEST_CASES.keys())

def get_test_pytest_path(test_name):
    return TEST_CASES[test_name]

def register_test(name, pytest_path):
    """
    pytest_path must be FILE PATH ONLY (no ::test_name)
    """
    TEST_CASES[name] = pytest_path
