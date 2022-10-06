# https://docs.python.org/3/library/enum.html
from enum import Enum, unique, auto

class Shape1(Enum):
    SQUARE = 2
    # SQUARE = 3

# ValueError: duplicate values found in <enum 'Shape2'>: RECTANGLE -> SQUARE
# @unique
# class Shape2(Enum):
#     SQUARE = 2
#     RECTANGLE = 2

print(Shape1['SQUARE']) # Shape1[name]
print(Shape1(2)) # Shape1(value) 


class Shape(Enum):
    SQUARE = 2 # (name: 'SQUARE', value: 2)
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2


print("----------------------------")
print(Shape['SQUARE'].name)
print(Shape['ALIAS_FOR_SQUARE'].name)
print(Shape['SQUARE'].value)
print(Shape['ALIAS_FOR_SQUARE'].value)
print(id(Shape['SQUARE']) == id(Shape['ALIAS_FOR_SQUARE']))


# class AutoName(Enum):
#     def _generate_next_value_(name, start, count, last_values):
#         # name, value
#         return name

# class Ordinal(AutoName):
#     NORTH = auto() # 'NORTH' , value: 'NORTH'
#     SOUTH = auto()
#     EAST = auto()
#     WEST = auto()

class Ordinal(Enum):
    def _generate_next_value_(name, start, count, last_values):
        # name, value
        return name + "_Asghar"
    """
    {
        'NORTH': Oridinal.NORTH(name, value),
        'SOUTH': Oridinal.SOUTH(name, value)
    }
    
    """
    NORTH = auto() # 'NORTH' , value: 'NORTH'
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


print(list(Ordinal))

for name, member in Ordinal.__members__.items():
    print(name, member.name, member.value)


print("----------------------------")
Animal = Enum('Animal', 'ANT BEE CAT DOG')
print(Animal)
print(Animal.ANT)
print(Animal.ANT.value)

print(list(Animal))