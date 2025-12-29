# TEST_CASES = {
#     "Google Maps - Coffee Shop Test":"tests/test_coffee_maps.py::test_open_maps_and_click_coffee",
#     "Google Maps - Check Route Navigation":"tests/test_route_navigation.py::test_route_to_hsr_with_gps_simulation"
# }

# def list_test_cases():
#     """Returns a list of available test case names."""
#     return list(TEST_CASES.keys())

# def get_test_pytest_path(test_name):
#     """Return full pytest node id"""
#     return TEST_CASES[test_name]

# def register_test(test_name, pytest_path):
#     TEST_CASES[test_name] = pytest_path

TEST_CASES = {
    "Google Maps - Coffee Shop Test": "tests/test_coffee_maps.py::test_open_maps_and_click_coffee",
    "Google Maps - Check Route Navigation": "tests/test_route_navigation.py::test_route_to_hsr_with_gps_simulation"
}

def list_test_cases():
    return list(TEST_CASES.keys())

def get_test_pytest_path(test_name):
    return TEST_CASES[test_name]

def register_test(name, pytest_path):
    TEST_CASES[name] = pytest_path
