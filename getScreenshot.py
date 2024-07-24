# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES

# For screenshots
import pyautogui
import datetime
import time

# --------------------------------------------------------------------------------------------------------

# Getting Screenshots
def capture_screenshot():
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time to be used in the filename
    formatted_now = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Define the filename with the formatted date and time
    filename = f"screenshot_{formatted_now}.png"

    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot with the filename
    screenshot.save(filename)
    return filename


# Example usage
# def capture_ss_at_interval(interval, num):
#     for i in range(num):
#         capture_screenshot()
#         time.sleep(interval)
        
# capture_ss_at_interval(5,3)