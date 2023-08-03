# ValueError
# Traceback (most recent call last):
#   File "c:\Users\MFT SERVER\Desktop\python\advanced_python2\08\06_exception.py", line 3, in <module>
#     raise ZeroDivisionError()
# ZeroDivisionError

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "c:\Users\MFT SERVER\Desktop\python\advanced_python2\08\06_exception.py", line 6, in <module>
#     raise ValueError()
# ValueError

# try:
#     raise ZeroDivisionError()
# except ZeroDivisionError as e:
#     print("ValueError")
#     raise ValueError()

# try:
#     raise ZeroDivisionError()
# except ZeroDivisionError as e:
#     print("ValueError")
#     raise ValueError() from None


# def run_me():
#     try:
#         raise ZeroDivisionError()
#     except ZeroDivisionError as e:
#         print("ValueError")
#         return ValueError("hello")

# print(run_me())


try:
    raise ZeroDivisionError()
except ZeroDivisionError as e:
    raise ValueError() from OSError()