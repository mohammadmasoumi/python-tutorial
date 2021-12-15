from enum import IntEnum


class Shape(IntEnum):
    SQUARE = 4
    TRIANGLE = 3
    OVAL = 5


for shape in Shape:
    print(shape, shape.name, shape.value)