import src.farm.fishing as fishing
import time

avialableOptions = ["1", "9"]

def main():
    print("Hello~")
    selectedOption = showOptions()
    while validateOption(selectedOption, avialableOptions) == False:
        selectedOption = showOptions()
    executeOption(selectedOption)

def showOptions():
    print("--------------------")
    print("1- Fishing spots")
    print("9- Exit")
    print("--------------------")
    print("What do you want to do")
    selectedOption = input("Select an option: ")
    return selectedOption


def validateOption(option, avialableOptions):
    for avialableOption in avialableOptions:
        if(avialableOption == option):
            return True
    return False

def executeOption(option):
    if(option == "1"):
        fishing.startFishingloop()
    if(option == "9"):
        print("Good bye")

main()