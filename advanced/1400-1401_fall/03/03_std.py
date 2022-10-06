import sys
from time import sleep

# no newline
# sys.stdout = open('../02/log.txt', )
temp = sys.stdout

# --------------------------------
sys.stdout = open('log.py', 'w')
print("print('Hello')")
# print("Hello")
# sys.stdout.write("Hello")
# sys.stdout.write("Hello")
sys.stdout.close()
# --------------------------------

# sleep(5)
# sys.stdout.write("Hello")
# print("Hello")
# temp.write("Hello")
