from enum import Enum, IntEnum

class Shape(Enum):
    RECTANGLE = "rect"
    TRIANGLE = "tri"
    CICLE = "circ"

print(Shape.RECTANGLE == "rect")
print(Shape.RECTANGLE.value == "rect")

print("--------------------")
class Color(IntEnum):
    RED = "1" # int("1") (name, value)
    BLUE = "2"
    YELLOW = "3"
    ALIAS_RED = "1"


class Direction(IntEnum):
    RIGHT = 1 # (name, value)
    LEFt = 2
    UP = 3
    DOWN = 4


print(Color.RED == 1)
print(Color.RED is Color.RED)
print(Color.RED is Color.ALIAS_RED)
print(Color.RED is Color.BLUE)
print(Color.RED is not Color.BLUE)
# print(Color.RED.value == 1) DO NOT NEED THAT
print("------------------------")

print(Color.RED is Direction.RIGHT)
print(Color.RED == Direction.RIGHT)

