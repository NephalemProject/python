import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A, S, Q, F
from fastai.vision.all import *
import numpy as np
import pyautogui

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

def label_func(x): return x.parent.name

learn_inf = load_learner("D:/Nephalem/Documents/uniteTrainingData/createImages/model01.pkl")
print("Loaded model! Press 'B' to begin AI.")

# Sleep time after actions
sleepy = 0.5

enemyDetected = False
global image

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(3)

def findEnemies():
    
    frame = image.astype(np.uint8)
    cv2.imwrite('curFrame.jpg', frame)

    # read image
    img = cv2.imread('curFrame.jpg')

    # set red range
    lowcolor = (220,100,40)
    highcolor = (255,135,80)

    # threshold
    thresh = cv2.inRange(img, lowcolor, highcolor)
    # count number of white pixels and test if zero
    count = np.sum(np.nonzero(thresh))

    if count == 0:
        enemyDetected = False
        print("No enemies")
    else:
        enemyDetected = True
        print("Enemy spotted = ", count)

while True:

    # pyautogui.click(1125, 545)

    image = grab_screen(region=(50, 100, 1100, 680))
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image,(224,224))
    # cv2.imshow("AI Analysis", image)
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    old_action = action
    # print(result[2][0].item(), result[2][1].item(), result[2][2].item(), result[2][3].item(), result[2][4].item())

    if action == "Up": # or result[2][0]>.1
        print(f"Up! - {result[1]}")
        keyboard.press("w")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("s")
        keyboard.release("q")
        keyboard.release("f")
        keyboard.release("e")
        time.sleep(sleepy)
        # pyautogui.click(1150, 80)

    if action == "Down": # or result[2][0]>.1
        print(f"Down! - {result[1]}")
        keyboard.press("s")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("q")
        keyboard.release("f")
        keyboard.release("e")
        time.sleep(sleepy)
        # pyautogui.click(1150, 80)

    elif action == "Left":
        print(f"LEFT! - {result[1]}")
        keyboard.press("a")
        keyboard.release("s")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("q")
        keyboard.release("f")
        time.sleep(sleepy)
        # pyautogui.click(1150, 80)

    elif action == "Right":
        print(f"Right! - {result[1]}")
        keyboard.press("d")
        keyboard.release("a")
        keyboard.release("s")
        keyboard.release("w")
        keyboard.release("q")
        keyboard.release("f")
        keyboard.release("e")
        time.sleep(sleepy)
        # pyautogui.click(1150, 80)

    findEnemies()

    if enemyDetected == False:
        action = "Right"
        continue

    if enemyDetected == True:
        if action == "Attack":
            print(f"Attacking! - {result[1]}")
            keyboard.press("e")
            keyboard.release("a")
            keyboard.release("s")
            keyboard.release("w")
            keyboard.release("q")
            keyboard.release("f")
            keyboard.release("w")
            time.sleep(sleepy)
            # pyautogui.click(1120, 70)

        elif action == "Move01":
            print("Using Move01 - {result[1]}")
            keyboard.press("q")
            keyboard.release("a")
            keyboard.release("d")
            keyboard.release("w")
            keyboard.release("s")
            keyboard.release("f")
            time.sleep(sleepy)
            keyboard.release("q")
            # pyautogui.click(1120, 70)

        elif action == "Move02":
            print("Using Move02 - {result[1]}")
            keyboard.press("f")
            keyboard.release("a")
            keyboard.release("d")
            keyboard.release("w")
            keyboard.release("q")
            keyboard.release("s")
            keyboard.release("e")
            time.sleep(sleepy)
            keyboard.release("f")
            # pyautogui.click(1120, 70)

    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break
