from enum import Enum
from typing import Collection


class Color(Enum):

    RED = 'red'
    BLUE = 'blue'
    YELLOW = 'yellow'


# name and value
print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
print("----------------------")


# more information
print(repr(Color.RED))
print("----------------------")


# type
print(type(Color.RED))
print(isinstance(Color.RED, Color))
print("----------------------")