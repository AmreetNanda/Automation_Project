def detect_intent(prompt: str) -> str:
    p = prompt.lower()

    if "why" in p or "fail" in p:
        return "ANALYZE_FAILURE"

    if "run" in p and "test" in p:
        return "RUN_EXISTING"

    return "GENERATE_TEST"
