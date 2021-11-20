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

my_map = None


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

        self._bullets = []
        # self._weak_flowers = []
        # self._strong_flowers = []
        # self._sun_flowers = []
        # self._slow_zombies = []
        # self._fast_zombies = []
        self._zombies = []
        self._flowers = []

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

    @property
    def bullets(self):
        return self._bullets

    def add_bullet(self, bullet):
        self._bullets.append(bullet)

    def remove_bullet(self, bullet):
        self._bullets.remove(bullet)

    # @property
    # def armored_flowers(self):
    #     return self._armored_flowers
    #
    # def add_armored_flowers(self, flower):
    #     self._armored_flowers.append(flower)
    #
    # def remove_armored_flowers(self, flower):
    #     self._armored_flowers.remove(flower)

    @property
    def flowers(self):
        return self._flowers

    def add_flower(self, flower):
        self._flowers.append(flower)

    def remove_flower(self, flower):
        self._flowers.remove(flower)

    @property
    def zombies(self):
        return self._zombies

    def add_zombie(self, zombie):
        self._zombies.append(zombie)

    def remove_zombie(self, zombie):
        self._zombies.remove(zombie)


class Obj:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def add_to_map(self):
        global my_map

        if isinstance(self, Bullet):
            my_map.add_bullet(self)

        elif isinstance(self, Plant):
            my_map.add_flower(self)

        elif isinstance(self, Zombie):
            my_map.add_zombie(self)

        my_map.board[self._x][self._y].add_content(self)

    def remove_from_map(self):
        # cell: Cell = map.board[self._x][self._y]
        # cell.remove_content(self)
        global my_map
        if isinstance(self, Bullet):
            my_map.remove_bullet(self)

        my_map.board[self._x][self._y].remove_content(self)


class Movable(Obj):

    def movement(self, direction: int):
        global my_map
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

        if new_x < 0 or new_x >= my_map.height or new_y < 0 or new_y >= my_map.width:
            my_map.board[prev_x][prev_y].remove_content(self)
            my_map.remove_bullet(self)
        else:
            my_map.board[prev_x][prev_y].remove_content(self)
            my_map.board[new_x][new_y].add_content(self)
            self._x = new_x
            self._y = new_y


class Bullet(Movable):

    def __init__(self, x, y, speed, damage):
        self._speed = speed
        self._damage = damage
        super(Bullet, self).__init__(x, y)

    @property
    def damage(self):
        return self._damage

    def move(self):
        super(Bullet, self).movement(Direction.RIGHT.value)

    def remove(self):
        my_map.board[self.x][self.y].remove_content(self)
        my_map.remove_bullet(self)

    def __str__(self):
        return "*"


class Plant(Obj):
    def __init__(self, x, y, hp):
        self._hp = hp
        # self._symbol = symbol
        super(Plant, self).__init__(x, y)

    @property
    def hp(self):
        return self._hp

    # def __str__(self):
    #     return f"{self._symbol}"


class ArmoredFlower(Plant):
    def __init__(self, x, y, hp, attack_speed, attack_power):
        self._attack_speed = attack_speed
        self._attack_power = attack_power
        super(ArmoredFlower, self).__init__(x, y, hp)

    def shoot(self):
        bullet = Bullet(self._x, self._y + 1, 1, self._attack_power)
        bullet.add_to_map()


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

    def __str__(self):
        return "WF"


class StrongFlower(ArmoredFlower):

    def __init__(self, x, y):
        hp = 100
        attack_speed = 1  # فاصله زمانی بین شلیک ها
        attack_power = 50
        # self._symbol = "SF"
        super(StrongFlower, self).__init__(x, y, hp, attack_speed, attack_power)

    def __str__(self):
        return "SF"

    __repr__ = __str__


class Zombie(Movable):

    def __init__(self, x, y, hp, speed, attack_speed, attack_power):
        self._speed = speed
        self._hp = hp
        self._attack_speed = attack_speed
        self._attack_power = attack_power
        super(Zombie, self).__init__(x, y)

    @property
    def hp(self):
        return self._hp

    @property
    def speed(self):
        return self._speed

    def move(self):
        super(Zombie, self).movement(Direction.LEFT.value)

    def remove(self):
        my_map.board[self.x][self.y].remove_content(self)
        my_map.remove_zombie(self)

    def damage(self, bullet):
        self._hp -= bullet.damage
        bullet.remove()

        if self._hp <= 0:
            self.remove()


class SlowZombie(Zombie):

    def __init__(self, x, y):
        hp = 50
        speed = 2
        attack_speed = 2
        attack_power = 100
        super(SlowZombie, self).__init__(x, y, hp, speed, attack_speed, attack_power)

    def __str__(self):
        return "SZ"


class FastZombie(Zombie):

    def __init__(self, x, y):
        hp = 100
        speed = 1
        attack_speed = 1
        attack_power = 50
        super(FastZombie, self).__init__(x, y, hp, speed, attack_speed, attack_power)

    def __str__(self):
        return "FZ"


class Engine:

    def __init__(self):
        pass

    def run(self):
        global my_map
        my_map = Map(5, 10)
        my_map.initialize()

        weak_plant = WeakFlower(0, 0)
        weak_plant.add_to_map()
        weak_plant.shoot()

        slow_zombie = SlowZombie(0, 9)
        slow_zombie.add_to_map()

        counter = 1
        while True:
            my_map.print_board()
            sleep(1)

            # move bullets
            for bullet in my_map.bullets:
                bullet.move()

            for bullet in my_map.bullets:
                for zombie in my_map.zombies:
                    if bullet.x == zombie.x and bullet.y == zombie.y:
                        zombie.damage(bullet)

            # move zombies
            for zombie in my_map.zombies:
                if counter % zombie.speed == 0:
                    zombie.move()

            if counter == 10:
                break

            counter += 1


if __name__ == "__main__":
    engine = Engine()
    engine.run()
