# AAOS:
#   platformName: "Android"
#   automationName: "UiAutomator2"
#   deviceName: "AAOS_Emulator"
#   platformVersion: "12"
#   appPackage: "com.example.bigmart"
#   appActivity: "com.example.bigmart.MainActivity"
#   autoGrantPermissions: true
#   adbExecTimeout: 60000

# AAOS:
# {
#   "platformName": "Android",
#   "appium:automationName": "UiAutomator2",
#   "appium:platformVersion": "12",
#   "appium:deviceName": "AAOS_Emulator",
#   "appium:appPackage": "com.yourapp.package",
#   "appium:appActivity": "com.android.car.settings",
#   "appium:adbExecTimeout": 50000,
#   "appium:autoGrantPermissions": true
# }
# ---------------------------------------------------------------------
# --------------------------------------------------------------------
# from appium.options.android import UiAutomator2Options

# def get_android_options():
#     options = UiAutomator2Options()
#     options.platform_name = "Android"
#     # options.platform_version = "14"
#     options.platform_version = "13"
#     options.device_name = "emulator-5554"
#     options.uuid = "emulator-5554"
#     options.automation_name = "UiAutomator2" 
#     options.no_reset = True
#     options.new_command_timeout = 300

#     # Target app
#     options.app_package = "com.google.android.apps.maps"
#     options.app_activity = "com.google.android.maps.MapsActivity"

#     return options

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

