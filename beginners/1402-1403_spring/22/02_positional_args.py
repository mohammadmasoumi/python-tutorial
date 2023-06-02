"""
positional argument
keyword arguement
"""


def add(a: int, b: str, c: int):  # a, b params
    # matching in python
    # a, b = 10, "ali"
    return str(a) + (b * 2) + str(c)


# positional argument
print(add(10, "ali", 10))  # 10, 12 args
# print(add("ali", 10))

# print("hello", end="", sep="")
# sorted([], key=function)
# a = 10
# conbination
# positional + keyword
print(add(10, c=10, b="ali"))
# TypeError: add() got multiple values for argument 'a'
# print(add(10, c=10, a="ali"))
# print(add(c=10, b="ali", 10))
