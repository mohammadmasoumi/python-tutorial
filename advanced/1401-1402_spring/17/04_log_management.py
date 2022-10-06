import sys


sys.stdout = open("log.txt", "a")

print("hello world1")
print("hello world2")
print("hello world3")

sys.stdout.close()
