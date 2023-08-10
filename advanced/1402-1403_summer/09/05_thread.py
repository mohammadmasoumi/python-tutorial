import threading
import time


"""

main thread  new thread
    |           |
    |           |
    |           |
    |           |
"""

bombs = []
def bomb_explosion():
    while True:
        for bomb in bombs:
            if bomb.timer > 2:
                bomb.exploid()

worm = None
def move_forward():
    while True:
        time.sleep(0.5)
        worm.move_forward()


# created thread
def say_hello():
    while True:
        time.sleep(1)
        print("Hello ...")


thread = threading.Thread(name="side-thread" ,target=say_hello)
thread.start()

# main thread
def say_bye():
    while True:
        time.sleep(1.1)
        print("Bye ...")

say_bye()