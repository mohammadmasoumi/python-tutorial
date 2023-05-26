from enum import Enum

# variable VS constant

# convension
# fully uppercase separated with _

# RIGHT
# RIGHT_DIRECTION
CELL_WIDTH = 11

# constant
RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'

# dict
Direction = {
    "RIGHT": 1,
    "LEFT": 2,
    "UP": 3,
    "DOWN": 4,
}

# class
class Direction:
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# packing 
# subset of a collection
Direction.RIGHT
Direction.LEFT

direction = RIGHT
if direction == RIGHT:
    print("Hello")

bomberman_direction = RIGHT
bomberman_direction = 1

# PREVENT MAKING MISTAKE
# MAKE IT EASIER

# class Direction(Enum):

