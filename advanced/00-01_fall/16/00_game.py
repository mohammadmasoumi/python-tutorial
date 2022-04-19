"""
board
[
height
 0  [       width          ]
 1  []
 2  []
 3  []
]
"""
import os
from time import sleep
from enum import IntEnum


# my_map = None


class Direction(IntEnum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Cell:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._contents = []

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def add_content(self, obj):
        self._contents.append(obj)

    def remove_content(self, obj):
        self._contents.remove(obj)

    def __str__(self):
        return " ".join([str(content) for content in self._contents]).center(11)


class Map:

    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._board = []

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def board(self):
        return self._board

    def initialize(self):
        for y in range(self._height):
            row = []
            for x in range(self._width):
                cell = Cell(x=x, y=y)
                row.append(cell)

            self._board.append(row)

    def print_board(self):
        roof = "-" * (self._width * (self._width + 2) + 1)
        print(roof)
        for y in range(self._height):
            print("|" + "|".join([str(cell) for cell in self._board[y]]) + "|")
            print(roof)
        print()


class Movable:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def movement(self, map: Map, direction: int):
        prev_x = self._x
        prev_y = self._y

        if direction == Direction.RIGHT.value:
            new_x = self._x
            new_y = self._y + 1

        elif direction == Direction.LEFT.value:
            new_x = self._x
            new_y = self._y - 1

        elif direction == Direction.UP.value:
            new_x = self._x - 1
            new_y = self._y

        elif direction == Direction.DOWN.value:
            new_x = self._x + 1
            new_y = self._y
        else:
            print(f"Invalid direction. {direction}")
            return

        if new_x < 0 or new_x > map.width or new_y < 0 or new_y > map.height:
            map.board[prev_x][prev_y].remove_content(self)
        else:
            map.board[prev_x][prev_y].remove_content(self)
            map.board[new_x][new_y].add_content(self)
            self._x = new_x
            self._y = new_y


class Bullet(Movable):

    def __init__(self, x, y, speed, damage):
        self._speed = speed
        self._damage = damage
        super(Bullet, self).__init__(x, y)

    def move(self, map: Map):
        super(Bullet, self).movement(map, Direction.RIGHT.value)

    def add_to_map(self, map: Map):
        map.board[self._x][self._y].add_content(self)

    def __str__(self):
        return "*"


class Plant:
    def __init__(self, x, y, hp):
        self._x = x
        self._y = y
        self._hp = hp

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def hp(self):
        return self._hp


class ArmoredFlower(Plant):
    def __init__(self, x, y, hp, attack_speed, attack_power):
        self._attack_speed = attack_speed
        self._attack_power = attack_power
        super(ArmoredFlower, self).__init__(x, y, hp)

    def shoot(self):
        pass


class SunFlower(Plant):
    def __init__(self, x, y):
        hp = 100
        self._score = 25
        super(SunFlower, self).__init__(x, y, hp)


class WeakFlower(ArmoredFlower):

    def __init__(self, x, y):
        hp = 100
        attack_speed = 2  # فاصله زمانی بین شلیک ها
        attack_power = 50
        super(WeakFlower, self).__init__(x, y, hp, attack_speed, attack_power)


class StrongFlower(ArmoredFlower):

    def __init__(self, x, y):
        hp = 100
        attack_speed = 1  # فاصله زمانی بین شلیک ها
        attack_power = 50
        super(StrongFlower, self).__init__(x, y, hp, attack_speed, attack_power)


class Engine:

    def __init__(self):
        pass

    def run(self):
        my_map = Map(5, 10)
        my_map.initialize()

        bullet = Bullet(0, 0, 1, 20)
        bullet.add_to_map(my_map)
        my_map.print_board()

        while True:
            sleep(1)
            bullet.move(my_map)
            my_map.print_board()
            break


if __name__ == "__main__":
    engine = Engine()
    engine.run()
