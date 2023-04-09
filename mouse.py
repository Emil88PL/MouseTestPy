import pyautogui
import time
import random

while True:
    # move the mouse cursor slightly
    pyautogui.moveTo(random.randint(0,100), random.randint(0,720))
    # wait for 2 minutes before moving again
    time.sleep(12)
print('knock knock')