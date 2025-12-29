# from framework.test_registry import register_test

# def auto_register(test_file_path, user_request):
#     test_name = f"AI: {user_request}"
#     pytest_path = f"{test_file_path}::test_ai_generated"
#     register_test(test_name, pytest_path)


from framework.test_registry import register_test
import os

def auto_register(test_path, user_prompt):
    test_name = f"AI: {user_prompt[:40]}"
    register_test(test_name, test_path)
