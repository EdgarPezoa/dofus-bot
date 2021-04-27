from pyautogui import * 
import pyautogui 
import time 
import random
import keyboard
from playsound import playsound

def getMousePosition():
    while 1:
        pos = pyautogui.position()
        print (pos);
        time.sleep(.4)

def getCurrentMousePosition():
    pos = pyautogui.position()
    print (pos)    

def pressToExit(lether):
    return keyboard.is_pressed(lether)