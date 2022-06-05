import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
from utils.directkeys import PressKey, ReleaseKey, W, D, A, S, E, Q, F

# Sleep time after actions
sleepy = 0.5

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

# Randomly pick action then sleep.
# 0 do nothing release everything ( except W )
# 1 hold left
# 2 hold right
# 3 Press Jump

while True:
    action = random.randint(0,6)

    if action == 0:
        print("Doing nothing....")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("e")
        keyboard.release("q")
        keyboard.release("f")
        time.sleep(sleepy)

    elif action == 1:
        print("Going left....")
        keyboard.press("a")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("e")
        keyboard.release("q")
        keyboard.release("f")
        time.sleep(sleepy)

    elif action == 2:
        print("Going right....")
        keyboard.press("d")
        keyboard.release("a")
        keyboard.release("w")
        keyboard.release("e")
        keyboard.release("q")
        keyboard.release("f")
        time.sleep(sleepy)

    elif action == 3:
        print("Going Down...")
        keyboard.press("s")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("e")
        keyboard.release("q")
        keyboard.release("f")
        time.sleep(sleepy)

    elif action == 4:
        print("Going up...")
        keyboard.press("w")
        keyboard.release("d")
        keyboard.release("a")
        keyboard.release("e")
        keyboard.release("q")
        keyboard.release("f")
        time.sleep(sleepy)

    elif action == 5:
        print("Move 1!")
        keyboard.press("q")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("e")
        keyboard.release("f")
        time.sleep(sleepy)

    elif action == 6:
        print("Move 2!")
        keyboard.press("f")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("e")
        keyboard.release("q")
        time.sleep(sleepy)

    elif action == 6:
        print("Attacking!")
        keyboard.press("e")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("q")
        keyboard.release("f")
        time.sleep(sleepy)





    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break
