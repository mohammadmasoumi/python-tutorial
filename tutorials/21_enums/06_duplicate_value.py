from enum import Enum, unique


class Shape(Enum):

    SQUARE1 = 2
    SQUARE2 = 2


print(Shape.SQUARE1)



@unique
class ForceDuplicateNotAllowed(Enum):
    TYPE1 = 1
    TYPE2 = 1


# ValueError: duplicate values found in <enum 'ForceDuplicateNotAllowed'>: TYPE2 -> TYPE1
print(ForceDuplicateNotAllowed.TYPE1)
print(ForceDuplicateNotAllowed.TYPE2)
