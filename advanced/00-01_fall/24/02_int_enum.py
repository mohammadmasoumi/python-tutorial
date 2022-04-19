from enum import IntEnum


class Color(IntEnum):
    RED = 1
    BLUE = 2
    pink = 3  # PINK
    # name: 'pink', value: 3


# [Color.RED] property name, value
print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
print(Color.pink.name)  # small pink
print(type(Color.pink.name))

color1 = 1
color2 = 'RED'
color3 = 'RED'

if color1 == Color.RED.value:
    print("I found red")

# color == Color.RED.value  <=> color == Color.RED
if color1 == Color.RED:
    print("I found red")

if color2 == Color.RED.name:
    print("my name is red")
