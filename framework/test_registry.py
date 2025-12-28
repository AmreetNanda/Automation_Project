TEST_CASES = {
    "Google Maps - Coffee Shop Test":"tests\test_coffee_maps.py",
    "Google Maps - Check Route Navigation":"tests\test_route_navigation.py"
}

def list_test_cases():
    """Returns a list of available test case names."""
    return list(TEST_CASES.keys())

def get_test_pytest_path(test_name):
    """Return full pytest node id"""
    return TEST_CASES[test_name]