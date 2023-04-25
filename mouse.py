import pyautogui
import time
import random

while True:
    # move the mouse cursor slightly
    pyautogui.moveTo(random.randint(0,100), random.randint(0,720))
    # wait for X sec before moving again
    
    time.sleep(12)


