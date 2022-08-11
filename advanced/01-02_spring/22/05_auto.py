from enum import Enum, auto


class Direction(Enum):
    RIGHT = auto()
    LEFT = auto()
    UP = auto()
    DOWN = auto()


# iterate
for key_name, item in Direction.__members__.items():
    # item: Direction.RIGHT
    # name: Direction.RIGHT.name #  RIGHT
    # value: Direction.RIGHT.value #  1
    # Direction.RIGHT_ALIAS.name
    print(key_name, item.name, item.value)





