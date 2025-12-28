from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_android_options():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    # options.platform_version = "14"  # optional, only if exact emulator version matches
    options.device_name = "emulator-5554"
    options.uuid = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.no_reset = True
    options.new_command_timeout = 300

    # Target apps (Google maps)
    options.app_package = "com.google.android.apps.maps"
    options.app_activity = "com.google.android.maps.MapsActivity"
    return options

