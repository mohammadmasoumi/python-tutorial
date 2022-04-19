from enum import Enum, unique

red = "red"
blue = 1

"""
1. mistake
2. forget
3. change the value
"""
if red == "reed":
    print("Hello red!")

if blue == 1:
    print("Hello blue")


# @unique
class Color(Enum):
    RED = 1
    BLUE = 3
    PINK = 3
    # ALTERNATIVE_PINK = 3


my_color = 2
if my_color == Color.RED.value:
    pass

RED = 1
BLUE = 2

for name, item in Color.__members__.items():
    print(name, item, item.value)
