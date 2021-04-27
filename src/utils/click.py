from pyautogui import * 
import pyautogui 
import time 
import random

minimunClickTime=.1
maximunClickTime=.23

minimunMovementTime=.5
maximunMovementTime=1

def mouseClick(x, y):
    pyautogui.moveTo(x, y, getMouseMovementSleepTime())
    pyautogui.mouseDown(button='right')
    time.sleep(getMouseClickSleepTime())
    pyautogui.mouseUp(button='right') 

def getMouseClickSleepTime():
    return random.uniform(minimunClickTime, maximunClickTime)

def getMouseMovementSleepTime():
    return random.uniform(minimunMovementTime, maximunMovementTime)