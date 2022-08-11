from enum import IntEnum


class Color1(IntEnum):
    RED = "1" # int("1")
    BLUE = "2"
    YELLOW = "3"


class Color2(IntEnum):
    RED = 1.1 # int(1.1)
    BLUE = 2.2
    YELLOW = 3.3


class Color3(IntEnum):
    RED = 1 
    BLUE = 2
    YELLOW = 3


print(Color1.RED.value, type(Color1.RED.value))
print(Color2.RED.value, type(Color2.RED.value))
print(Color3.RED.value, type(Color3.RED.value))