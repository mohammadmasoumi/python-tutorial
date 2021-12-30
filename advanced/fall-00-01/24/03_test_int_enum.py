from enum import IntEnum

# ValueError: invalid literal for int() with base 10: 'mamad'
# print(int('mamad'))

print(ord('a'))
print(ord('A'))

# TypeError: ord() expected a character, but string of length 2 found
# print(ord('AB'))
print(chr(65))


# class Color0(IntEnum):
#     RED = 'red'  # try to cast to int
#     BLUE = 'blue'
#     pink = 'pink'


class Color1(IntEnum):
    RED = '1'
    BLUE = '2'
    pink = '3'


class Color2(IntEnum):
    RED = 1
    BLUE = 2
    pink = 3


class Color3(IntEnum):
    RED = 1.3
    BLUE = 2.4
    pink = 3.9


print(type(Color1.RED.value))
print(type(Color2.RED.value))
print(type(Color3.RED.value))

if '1' == Color1.RED.value:
    print("I found RED 1")

if 1 == Color1.RED.value:
    print("I found RED 2")

if 1 == Color3.RED.value:
    print("I found RED 3")
