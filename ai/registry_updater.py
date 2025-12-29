from framework.test_registry import register_test

def auto_register(test_file_path, user_request):
    test_name = f"AI: {user_request}"
    pytest_path = f"{test_file_path}::test_ai_generated"
    register_test(test_name, pytest_path)
