"""

Error handling
Exception

try, catch
keywords: try, except (obligation)
keywords: else, finally (optional)

"""

"""
Traceback (most recent call last):
  File "C:/Users/mft/Desktop/Advanced Python/18/07_handling_exception.py", line 17, in <module>
    print(a / 0)
ZeroDivisionError: division by zero
"""

# print(int('a'))
# ValueError: invalid literal for int() with base 10: 'a'

"""
try:

raise exception
#do not execute this lines

:except

1. raise exception
2. => except for catching exception
3. should catch, it will catch the exception
"""

while True:
    try:
        # code block

        a = int(input())  # do not execute the rest of code

        # print(a / 0)
        break

    except ValueError:
        print("Ops, wrong int! Try again.")
