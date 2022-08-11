# Direction
RIGHT = "راست" # right
LEFT = "left" # no momery efficiency
UP = 3 # "up"
DOWN = "down"
ASGHAR_ABAD = ""
MY_RIGHT = "right"
RIGHT_ALIAS = "right"

DIRECTIONS =  [RIGHT, LEFT, UP, DOWN, ASGHAR_ABAD]

# Polar Direction 
SOUTH = "south"
NORTH = "north"
WEST = "west"
EAST = "east"
ASGHAR_POLAR = "asghar_polar"

DIRECTIONS_POLAR = [SOUTH, NORTH, WEST ,EAST ,ASGHAR_POLAR]

from enum import Enum

class PolarDirection(Enum):
    SOUTH = "south"
    NORTH = "north"
    WEST = "west"
    EAST = "east"
    ASGHAR_POLAR = "asghar_polar"


print(PolarDirection)
print(PolarDirection.SOUTH)
print(PolarDirection.SOUTH.name)
print(PolarDirection.SOUTH.value)

# only support == and !=
print(PolarDirection.SOUTH == PolarDirection.EAST)
# TypeError: '>' not supported between instances of 'PolarDirection' and 'PolarDirection'
# print(PolarDirection.SOUTH > PolarDirection.EAST)


