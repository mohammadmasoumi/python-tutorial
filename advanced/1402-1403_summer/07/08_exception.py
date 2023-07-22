

class SafaviGrandGrandFatherException(BaseException):

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__()

    def __str__(self):
        return f"{self.code}: {self.message}"


class SafaviGrandFatherException(SafaviGrandGrandFatherException):
    pass


class SafaviFatherException(SafaviGrandFatherException):
    pass


class SafaviException(SafaviFatherException):
    pass


e = SafaviException(code=400, message="")

print(isinstance(e, SafaviGrandGrandFatherException))


# n = input()

# try:
#     if n != "safavi":
#         raise SafaviException(code="500", message="you must enter safavi.")
# except SafaviGrandGrandFatherException:
#     print("SafaviGrandGrandFatherException has occured!")
# except SafaviGrandFatherException:
#     print("SafaviGrandFatherException has occured!")
# except SafaviFatherException:
#     print("SafaviFatherException has occured!")
# except SafaviException:
#     print("SafaviException has occured!")


# CORRECT ONE

# order of exception chain is important
# because SafaviException is an instance of GrandGrandFatherSafaviException
# so you must check SafaviException first in the Safavi's inheritance chain.
n = input()

try:
    if n != "safavi":
        raise SafaviException(code="500", message="you must enter safavi.")
except SafaviException:
    print("SafaviException has occured!")
except SafaviFatherException:
    print("SafaviFatherException has occured!")
except SafaviGrandFatherException:
    print("SafaviGrandFatherException has occured!")
except SafaviGrandGrandFatherException:
    print("SafaviGrandGrandFatherException has occured!")


# n = input()

# try:
#     if n != "safavi":
#         raise SafaviException(code="500", message="you must enter safavi.")
# except BaseException:
#     print("SafaviException has occured!")
# except SafaviFatherException:
#     print("SafaviFatherException has occured!")
# except SafaviGrandFatherException:
#     print("SafaviGrandFatherException has occured!")
# except SafaviGrandGrandFatherException:
#     print("SafaviGrandGrandFatherException has occured!")
