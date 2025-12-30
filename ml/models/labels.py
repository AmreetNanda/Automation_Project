from enum import Enum

class FailureType(str, Enum):
    LOCATOR_NOT_FOUND = "locator_not_found"
    APP_NOT_LAUNCHED = "app_not_launched"
    TIMEOUT = "timeout"
    PERMISSION_DENIED = "permission_denied"
    UNKNOWN = "unknown"
