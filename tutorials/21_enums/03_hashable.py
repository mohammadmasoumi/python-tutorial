from enum import Enum


class Color(Enum):

    RED = 'red'
    YELLOW = 'yellow'
    BLUE = 'blue'


apples = {}
apples[Color.RED] = 'red is delicious'
apples[Color.YELLOW] = 'yellow is shinning'


print(apples)
print(apples[Color.RED])
# print(apples[Color.RED.name]) raise exception