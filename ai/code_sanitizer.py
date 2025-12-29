import re

def strip_code_fences(code: str) -> str:
    """
    Removes ```python ... ``` or ``` ... ``` wrappers if present
    """
    # Remove opening fence
    code = re.sub(r"^```(?:python)?\s*", "", code.strip(), flags=re.IGNORECASE)

    # Remove closing fence
    code = re.sub(r"\s*```$", "", code.strip())

    return code
