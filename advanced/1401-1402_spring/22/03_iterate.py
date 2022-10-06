from enum import Enum

class Direction(Enum):
    RIGHT = 1
    RIGHT_ALIAS = 1
    LEFT = 2
    UP = 3
    DOWN = 4


# iterate
for key_name, item in Direction.__members__.items():
    # item: Direction.RIGHT
    # name: Direction.RIGHT.name #  RIGHT
    # value: Direction.RIGHT.value #  1
    # Direction.RIGHT_ALIAS.name
    
    # The same place in memory
    # RIGHT, RIGHT_ALIAS
    # {
    #   "name": "RIGHT",
    #   "value": 1
    # }
    print(key_name, item.name, item.value)


print([key_name for key_name, item in Direction.__members__.items() if key_name != item.name])



