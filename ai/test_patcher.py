import re

def patch_test_code(file_path, old, new):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    code = code.replace(
        f"driver.find_element({old['by']}, \"{old['value']}\")",
        f"driver.find_element({new['by']}, \"{new['value']}\")"
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
