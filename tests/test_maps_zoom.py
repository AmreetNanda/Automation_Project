import time
from utils.driver_setup import create_driver, quit_driver
from logger import logging

def test_zoom_in_and_out():
    driver = create_driver()
    try:
        time.sleep(2)

        size = driver.get_window_size()
        x = size["width"]
        y = size["height"]

        region = {
            "left": int(x * 0.25),
            "top": int(y * 0.25),
            "width": int(x * 0.5),
            "height": int(y * 0.5),
            "percent": 0.55,
            "speed": 200
        }

        print("Pinching (zoom-out)...")
        driver.execute_script("mobile: pinchCloseGesture", region)
        logging.info("Pinching (zoom-out)....")
        time.sleep(1)

        print("Pinching (zoom-out)...")
        driver.execute_script("mobile: pinchCloseGesture", region)
        logging.info("Pinching (zoom-out)....")
        time.sleep(1)

        print("Zooming In...")
        driver.execute_script("mobile: pinchOpenGesture", region)
        logging.info("Zooming in....")
        time.sleep(1)

        print("Zooming In...")
        driver.execute_script("mobile: pinchOpenGesture", region)
        logging.info("Zooming in....")
        time.sleep(1)

        #close Google maps and return to Home
        driver.terminate_app("com.google.android.apps.maps")
        driver.press_keycode(3) #Home button
        logging.info("Returned to Home screen")
    
    finally:
        quit_driver(driver)

