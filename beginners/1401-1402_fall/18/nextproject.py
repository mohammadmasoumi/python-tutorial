import pyautogui
import time


class khiabon:
    def __init__(self, k_blocks,):
        self.k_blocks = k_blocks


class car:
    def __init__(self, position):
        self.position = position

    def go(self):
        if position == khiabon(k_blocks):
            pyautogui.alert("u reached ur desteny")
            exit()
        if pyautogui.press("w"):
            print("car is running...")
            time.sleep(2)
            self.position += 1
            print(f"car positon is {self.position}")
        elif pyautogui.press("s"):
            if position == 0:
                pyautogui.alert("bro dont do it or ur gonna break ur car")
            print("car is backing...")
            time.sleep(2)
            self.position -= 1
            print(f"car positon is {self.position}")


cor = car(0)
print(cor)
