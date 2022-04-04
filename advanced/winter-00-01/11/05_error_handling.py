"""
Traceback (most recent call last):
  File "c:/Users/MFT SERVER/Desktop/python/advanced-python2/11/05_error_handling.py", line 4, in <module>
    print(12 / a)
ZeroDivisionError: division by zero

Traceback (most recent call last):
  File "c:/Users/MFT SERVER/Desktop/python/advanced-python2/11/05_error_handling.py", line 9, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'A'
"""

try:
    a = int(input())
    print(12 / a)

except (ZeroDivisionError, ValueError):
    print("Invalid")


