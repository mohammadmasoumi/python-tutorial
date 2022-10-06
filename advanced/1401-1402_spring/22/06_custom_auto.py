from enum import Enum, auto


class Direction(Enum):

    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    RIGHT = auto() # right, 1
    LEFT = auto() # left, 2
    UP = auto()
    DOWN = auto()


# iterate
for key_name, item in Direction.__members__.items():
    # item: Direction.RIGHT
    # name: Direction.RIGHT.name #  RIGHT
    # value: Direction.RIGHT.value #  1
    # Direction.RIGHT_ALIAS.name
    print(f"{item.name}: {item.value}", )





