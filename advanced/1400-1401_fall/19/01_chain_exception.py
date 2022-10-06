# # Chain exception
# """
# Traceback (most recent call last):
#   File "C:/Users/mft/Desktop/Advanced Python/19/01_chain_exception.py", line 4, in <module>
#     n = int(input())
# ValueError: invalid literal for int() with base 10: 'a'
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "C:/Users/mft/Desktop/Advanced Python/19/01_chain_exception.py", line 7, in <module>
#     raise RuntimeError("This is an exception") from exc
# RuntimeError: This is an exception
# """
import sys


class CustomException(Exception):
    def __init__(self, desc, error_code):
        self.desc = desc
        self.error_code = error_code


sys.tracebacklimit = None

try:
    char = input()

    # check whether this string is uppercase or not
    if char.isupper():
        # raise CustomException(f"This is an uppercase. {char}")
        raise CustomException(f"خطایی رخ داده است. لطفا بعدا تلاش کنید.{char}", 400)

except CustomException as exc:
    print(exc.args)
    print(exc.desc)
    print(exc.error_code)
    # SystemExit(exc)

    raise ValueError(exc.desc) from None

    # raise ConnectionError("This is an exception") from None  # disable chain exception
    # print(exc.args)

    # raise RuntimeError("This is an exception") from ConnectionError  # chain exception implicitly
    # raise RuntimeError("This is an exception") from exc  # chain exception implicitly

# print(int("A"))
