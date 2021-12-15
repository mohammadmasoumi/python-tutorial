from enum import Enum
from typing import Collection


class Color(Enum):

    RED = 'red'
    BLUE = 'blue'
    YELLOW = 'yellow'


print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
print(repr(Color.RED))

