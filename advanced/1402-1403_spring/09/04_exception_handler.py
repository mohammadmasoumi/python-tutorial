# 1. 
# try:
#     a = 5/0
# except ZeroDivisionError:
#     print("I got this exception")
#     print("Write some queries on the DB")
#     raise RuntimeError('Error')

# Traceback (most recent call last):
#   File "c:\Users\MFT SERVER\Desktop\Python\advanced-python-winter1401\08\04_exception_handler.py", line 3, in <module>
#     a = 5/0
# ZeroDivisionError: division by zero

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "c:\Users\MFT SERVER\Desktop\Python\advanced-python-winter1401\08\04_exception_handler.py", line 5, in <module>
#     raise RuntimeError('Error')
# RuntimeError: Error

# 2.
# try:
#     a = 5/0
# except ZeroDivisionError:
#     raise RuntimeError('Error') from None

# Traceback (most recent call last):
#   File "c:\Users\MFT SERVER\Desktop\Python\advanced-python-winter1401\08\04_exception_handler.py", line 25, in <module>
#     raise RuntimeError('Error') from None
# RuntimeError: Erro

# 3.
try:
    a = 5/0
except ZeroDivisionError:
    raise RuntimeError('Error') from ValueError()

# ValueError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "c:\Users\MFT SERVER\Desktop\Python\advanced-python-winter1401\08\04_exception_handler.py", line 36, in <module>
#     raise RuntimeError('Error') from ValueError()
# RuntimeError: Error