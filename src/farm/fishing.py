from src.utils import click, utils
from playsound import playsound
from pyautogui import * 
import pyautogui 
import time 
import random

fishing_spot_image = 'src/resources/fish_spot.png'
fishingTime = 11.2
fishingMovementTime = 2
deltaTime = 2

minimunClickTime =.5
maximunClickTime = 1

pixelSkip = 3

def getFishingSleepTime():
    return random.uniform(
        fishingTime + fishingMovementTime,
        fishingTime + fishingMovementTime + deltaTime
    )

def getFishingClickSleepTime():
    return random.uniform(
        minimunClickTime,
        maximunClickTime
    )

def getFishSpot():
    fishSpot = pyautogui.locateOnScreen(fishing_spot_image, grayscale=False, confidence=0.5)
    if(fishSpot):
        print("Fishing...")
        click.mouseClick(
            fishSpot.left + ( fishSpot.width / 2 ),
            fishSpot.top + ( fishSpot.height / 2 )
        )
    else:
        print("Nothing to fish")
        playsound('src/resources/beep.wav')

def getFishSpots():
    fishSpots = pyautogui.locateAllOnScreen(fishing_spot_image, grayscale = False, confidence = 0.5)
    lastPos = None
    if(fishSpots):
        print("Fishing...")
        for spot in fishSpots:
            if(compareFishingSpots(lastPos, spot)):
                continue;
            if(utils.pressToExit('q')):
                break;
            click.mouseClick(
                spot.left + ( spot.width / 2 ),
                spot.top + ( spot.height / 2 )
            )
            lastPos = spot
            time.sleep(getFishingClickSleepTime())
        print("Fishing ended")
        playsound('src/resources/beep.wav')
        
        
def compareFishingSpots(first, second):
    if(first):
        return (((first.left + 1 == second.left) or (first.left + 2 == second.left)) and (first.top == second.top))
    else:
        return False

def startFishingloop():
    print("Fishing loop started...")
    while utils.pressToExit('q') == False:
        getFishSpot()
        time.sleep(getFishingSleepTime())