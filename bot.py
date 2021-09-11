import time
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *


class Cordinates():
    replayBtn = (341, 386)
    dinasaur = (370,390)


def restartGame():
    pyautogui.click(Cordinates.replayBtn)


def pressSapce():

    pyautogui.keyDown('space')
    print("jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')



def imageGrab():
    box = (
        190, 365,
        280, 419)

    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    print(a.sum())
    return a.sum()


def main():
    restartGame()
    while True:
        if (imageGrab() != 5107):
            pressSapce()
            time.sleep(0.1)

main()


