from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3


print(Color(1))
print(Color(3))

print(Color['RED'])
print(Color['GREEN'])
print('-----------------------------')


class ColorCode(Enum):
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'


print(ColorCode('red'))
print(ColorCode['RED'])