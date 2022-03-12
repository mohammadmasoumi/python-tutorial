# calculator

"""
Multi-line comment

Supported operators:
+, -, *, /
1. input
    num: 2
    opt: +
    num: 3
2. 
if opt == "+":
    print(num1 + num2)

WRONG
# num1 opt num
"""

num1 = int(input())
opt = input() # "+", "-"
num2 = int(input())

"""
12
/
0
Traceback (most recent call last):
  File "c:/Users/MFT SERVER/Desktop/python/python beginners 1/04/06_calculator.py", line 29, in <module>
    elif opt == "*":
ZeroDivisionError: division by zero
"""

if opt == "+":
    print(num1 + num2)
    # 4 spaces - 1 tab
    # the same indentation
    # the same indentation
elif opt == "*":
    print(num1 * num2)
elif opt == "/":
    if num2 == 0:
        print("invalid operation")
    else:
        print(num1 / num2)
elif opt == "-":
    print(num1 - num2)

