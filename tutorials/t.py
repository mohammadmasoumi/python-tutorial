
from time import sleep

for i in range(1, 101):
    text = ""
    print(f"{text}\r", end="")
    print('█'*i, end="")
    sleep(0.3)