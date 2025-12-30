from dataclasses import dataclass
from typing import Optional

@dataclass
class TestExecutionSample:
    prompt: str
    generated_code: str
    pytest_log: str
    appium_log: str
    success: bool
    failure_reason: Optional[str]
