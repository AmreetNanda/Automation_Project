# # import re
# # import os

# # def normalize_appiumby(code: str) -> str:
# #     replacements = {
# #         r"\bAppiumAppiumID\b": "AppiumBy.ID",
# #         r"\bAppiumID\b": "AppiumBy.ID", 
# #         r"\bAppiumACCESSIBILITY_ID\b": "AppiumBy.ACCESSIBILITY_ID",
# #         r"\bAppiumAppiumACCESSIBILITY_AppiumID\b": "AppiumBy.ACCESSIBILITY_ID",
# #         r"\bACCESSIBILITY_ID\b": "AppiumBy.ACCESSIBILITY_ID",
# #     }

# #     for pattern, replacement in replacements.items():
# #         code = re.sub(pattern, replacement, code)
# #     return code

# # def ensure_required_blocks(code: str) -> str:
# #     """
# #     Ensure driver imports and SCREENSHOT_DIR setup exist
# #     """
# #     required_lines = [
# #         "from utils.driver_setup import create_driver, quit_driver",
# #         'SCREENSHOT_DIR = "screenshot"',
# #         "os.makedirs(SCREENSHOT_DIR, exist_ok=True)"
# #     ]

# #     for line in required_lines:
# #         if line not in code:
# #             code = line + "\n" + code

# #     return code

# # def final_locator_safety_pass(code: str) -> str:
# #     """
# #     Final pass to replace any remaining AppiumID or ACCESSIBILITY_ID with AppiumBy constants
# #     """
# #     hard_replacements = {
# #         "AppiumID": "AppiumBy.ID",
# #         "ACCESSIBILITY_ID": "AppiumBy.ACCESSIBILITY_ID",
# #     }

# #     for bad, good in hard_replacements.items():
# #         code = code.replace(bad, good)

# #     return code

# # def normalize_code(code: str) -> str:
# #     code = normalize_appiumby(code)
# #     code = ensure_required_blocks(code)
# #     code = final_locator_safety_pass(code)  # ✅ ensures no leftover AppiumID
# #     return code


# import re
# import os

# def normalize_appiumby(code: str) -> str:
#     replacements = {
#         r"\bAppiumAppiumID\b": "AppiumBy.ID",
#         r"\bAppiumID\b": "AppiumBy.ID", 
#         r"\bAppiumACCESSIBILITY_ID\b": "AppiumBy.ACCESSIBILITY_ID",
#         r"\bAppiumAppiumACCESSIBILITY_AppiumID\b": "AppiumBy.ACCESSIBILITY_ID",
#         r"\bACCESSIBILITY_ID\b": "AppiumBy.ACCESSIBILITY_ID",
#     }

#     for pattern, replacement in replacements.items():
#         code = re.sub(pattern, replacement, code)
#     return code

# def ensure_required_blocks(code: str) -> str:
#     """
#     Ensure driver imports and SCREENSHOT_DIR setup exist
#     """
#     required_lines = [
#         "from utils.driver_setup import create_driver, quit_driver",
#         'SCREENSHOT_DIR = "screenshot"',
#         "os.makedirs(SCREENSHOT_DIR, exist_ok=True)"
#     ]

#     for line in required_lines:
#         if line not in code:
#             code = line + "\n" + code

#     return code

# def final_locator_safety_pass(code: str) -> str:
#     """
#     Final pass to replace any remaining AppiumID or ACCESSIBILITY_ID with AppiumBy constants
#     """
#     hard_replacements = {
#         "AppiumID": "AppiumBy.ID",
#         "ACCESSIBILITY_ID": "AppiumBy.ACCESSIBILITY_ID",
#     }

#     for bad, good in hard_replacements.items():
#         code = code.replace(bad, good)

#     return code

# def normalize_code(code: str) -> str:
#     code = normalize_appiumby(code)
#     code = ensure_required_blocks(code)
#     code = final_locator_safety_pass(code)  
#     return code

import re

def normalize_appiumby(code: str) -> str:
    replacements = {
        r"\bAppiumAppiumID\b": "AppiumBy.ID",
        r"\bAppiumID\b": "AppiumBy.ID",
        r"\bAppiumACCESSIBILITY_ID\b": "AppiumBy.ACCESSIBILITY_ID",
        r"\bAppiumAppiumACCESSIBILITY_AppiumID\b": "AppiumBy.ACCESSIBILITY_ID",
        r"\bACCESSIBILITY_ID\b": "AppiumBy.ACCESSIBILITY_ID",
    }

    for pattern, replacement in replacements.items():
        code = re.sub(pattern, replacement, code)

    # Ensure driver setup import lines are present
    if "from utils.driver_setup import create_driver, quit_driver" not in code:
        code = "from utils.driver_setup import create_driver, quit_driver\n" + code

    if 'SCREENSHOT_DIR = "screenshot"' not in code:
        code = 'SCREENSHOT_DIR = "screenshot"\nos.makedirs(SCREENSHOT_DIR, exist_ok=True)\n' + code

    return code
