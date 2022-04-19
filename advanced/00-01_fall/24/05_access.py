from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    PINK = 3


# access
# Color[name]
# Color.RED
# Color.RED
print(Color['RED'])  # [name]
print(Color(1))  # (value)
print(Color(2))
