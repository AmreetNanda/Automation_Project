from dataclasses import dataclass
from typing import Optional

@dataclass
class LocatorEvent:
    test_name: str
    locator_type: str      # ID, ACCESSIBILITY_ID, XPATH
    locator_value: str
    success: bool
    screen: Optional[str]
