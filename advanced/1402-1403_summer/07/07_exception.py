
class SafaviException(BaseException):

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__()

    def __str__(self):
        return f"{self.code}: {self.message}"


n = input()

try:
    if n != "safavi":
        raise SafaviException(code="500", message="you must enter safavi.")
except SafaviException:
    print("safavi exception has occured!")

