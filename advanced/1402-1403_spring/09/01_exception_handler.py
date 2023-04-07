# as => alis

# from math import sqrt as my_sqrt

# with open('file.txt', 'r') as f:
#     pass


class MyCustomException(BaseException):

    def __init__(self, code, desc) -> None:
        super().__init__(code, desc)

        self.code = code 
        # description
        self.desc = desc

    def __str__(self) -> str:
        return f"code: {self.code}, desc: {self.desc}"


class MyInt(int):

    # magic function, dunder method //
    def __truediv__(self, o):
        if isinstance(o, int) and o == 0:
            raise MyCustomException(code=400, desc="ZeroDivisionException")

    def __floordiv__(self, o): # /
        if o == 0: # isinstance(o, int) and
            raise MyCustomException(code=400, desc="ZeroDivisionException")

# raise MyCustomException(code=400, desc="BadError")

# a = int(13)
# a = 13
try:
    n = int(input())
    m = MyInt(12)

    print(m / n)
    # print(n / m)

except ValueError:
    print("ValueError")
except MyCustomException as e:
    print("MyCustomException", e.code, e.desc, e)