from framework.test_registry import register_test
import os

def auto_register(test_path, user_prompt):
    test_name = f"AI: {user_prompt[:40]}"
    register_test(test_name, test_path)
