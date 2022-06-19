import time

CELL_WIDTH = 11
my_map = None


class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__contents = []

    @property
    def contents(self):
        return self.__contents

    def add_content(self, obj):
        self.__contents.append(obj)
    
    def remove_content(self, obj):
        self.__contents.remove(obj)
    
    def __str__(self):
        return "-".join(map(str, self.__contents)).center(CELL_WIDTH)


# cell = Cell(10, 10)
# cell.add_content(12)
# print(cell)

class Map:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.board = [[Cell(x=col, y=row) for col in range(self.width)] for row in range(self.length)]

    def print_map(self):
        # [Cell, Cell, Cell]
        """
        (11 + 1) * self.width + 1
        -----------------------------
        |      |      |      |      |
        -----------------------------
        """
        roof = (CELL_WIDTH + 1) * self.width + 1

        for row in self.board:
            print("-" * roof)
            print("|" + "|".join(map(str, row)) + "|")

        print("-" * roof)


class Zombie:
    
    def __init__(self, x, y, hp, damage, speed):
        self.x = x
        self.y= y
        self.hp = hp
        self.damage = damage
        self.speed = speed

class SlowZombie(Zombie):

    def __init__(self, x, y):
        hp = 100
        damage = 50
        speed = 2

        super().__init__(x, y, hp, damage, speed)
    
class FastZombie(Zombie):

    def __init__(self, x, y):
        hp = 50
        damage = 100
        speed = 1

        super().__init__(x, y, hp, damage, speed)
    

class Engine:

    def __init__(self) -> None:
        self.rnd = 0

    def run(self):
        global my_map

        my_map = Map(10, 10)
        my_map.print_map()

        while True:
            time.sleep(0.5)


            self.rnd = 0



engine = Engine()
engine.run()