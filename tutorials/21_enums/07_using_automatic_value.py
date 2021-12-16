from enum import Enum, auto


class Color(Enum):

    RED = auto()
    BLUE = auto()
    GREEN = auto()


print(Color.RED)
print(Color.BLUE)
print(Color.GREEN)


print(Color.RED.value)
print(Color.BLUE.value)
print(Color.GREEN.value)