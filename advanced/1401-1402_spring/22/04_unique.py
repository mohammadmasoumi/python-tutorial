from enum import Enum, unique


@unique
class Direction(Enum):
    RIGHT = 1
    # ValueError: duplicate values found in <enum 'Direction'>: RIGHT_ALIAS -> RIGHT
    # RIGHT_ALIAS = 1
    LEFT = 2
    UP = 3
    DOWN = 4


# iterate
for key_name, item in Direction.__members__.items():
    # item: Direction.RIGHT
    # name: Direction.RIGHT.name #  RIGHT
    # value: Direction.RIGHT.value #  1
    # Direction.RIGHT_ALIAS.name
    print(key_name, item.name, item.value)





