from enum import Enum


class Shape(Enum):

    SQUARE = 2
    SQUARE = 3


# TypeError: 'SQUARE' already defined as: 2
print(Shape.SQUARE)
    