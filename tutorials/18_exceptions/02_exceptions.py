"""
Built-in Exceptions

https://docs.python.org/3/library/exceptions.html#bltin-exceptions
"""

# print(10 * (1/0))
"""
Traceback (most recent call last):
  File "02_exceptions.py", line 3, in <module>
    print(10 * (1/0))
ZeroDivisionError: division by zero
"""

# print(4 + spam * 4)
"""
Traceback (most recent call last):
  File "02_exceptions.py", line 11, in <module>
    print(4 + spam * 4)
NameError: name 'spam' is not defined
"""

print('2' + 2)
"""
Traceback (most recent call last):
  File "02_exceptions.py", line 20, in <module>
    print('2' + 2)
TypeError: can only concatenate str (not "int") to str
"""