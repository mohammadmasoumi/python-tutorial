# ord

print(ord("A"))
print(chr(10000))
print(chr(10001))
print(chr(10002))
print(chr(10004))
print("😍😍😎😎")
print(ord("😎"))
print(chr(128527))

import time
for idx in range(100):
    time.sleep(0.3)
    load = "\r" + "█" * (idx+1) 
    print(load, end="")

# return carriage
print("hello\ra")
print("hello\rworld")
print("hello\rhell")
print("hello\rhelloo")