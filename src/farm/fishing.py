from src.utils import clickfn, utils, voiceSynthesizer
from playsound import playsound
from pyautogui import * 
import pyautogui 
import time 
import random

voice = voiceSynthesizer.VoiceSynthesizer()
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

def getFishSpots():
    fishSpots = list(pyautogui.locateAllOnScreen(fishing_spot_image, grayscale = False, confidence = 0.5))
    lastPos = None
    if(fishSpots):
        print("Fishing...")
        voice.readText("Fishing")
        for spot in fishSpots:
            if(compareFishingSpots(lastPos, spot)):
                continue;
            if(utils.pressToExit('q')):
                break;
            clickfn.mouseClick(
                spot.left + ( spot.width / 2 ),
                spot.top + ( spot.height / 2 )
            )
            lastPos = spot
            time.sleep(getFishingClickSleepTime())
    else:
        print("Nothing to fish...")
        playsound('src/resources/beep.wav')
        voice.readText("Nothing to fish")
    time.sleep(getFishingSleepTime())
 
def compareFishingSpots(first, second):
    if(first):
        return (((first.left + 1 == second.left) or (first.left + 2 == second.left)) and (first.top == second.top))
    else:
        return False

def startFishingloop():
    print("Fishing loop started...")
    while utils.pressToExit('q') == False:
        getFishSpots()