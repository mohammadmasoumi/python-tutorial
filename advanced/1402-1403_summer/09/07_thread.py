

import threading
import time

counter = 0


def critical_section():
    global counter
    counter += 1


# created thread
def say_hello():
    global counter
    while True:
        time.sleep(1)
        critical_section()

thread = threading.Thread(name="side-thread" ,target=say_hello)
thread.start()
# thread.join()

# main thread
def say_bye():
    global counter

    while True:
        time.sleep(1.5)
        critical_section()
        print(f"counter: {counter}")

say_bye()

