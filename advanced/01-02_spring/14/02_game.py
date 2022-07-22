import time
import random


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


    def add_content(self, obj, x, y):
        # Cell: self.board[y][x]
        self.board[y][x].add_content(obj)


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

    def move(self):
        new_x = self.x - 1

        if 0 <= new_x < my_map.width:
            my_map.board[self.y][self.x].remove_content(self)
            self.x = new_x
            my_map.board[self.y][self.x].add_content(self)
            

class SlowZombie(Zombie):

    def __init__(self, x, y):
        hp = 100
        damage = 50
        speed = 2

        super().__init__(x, y, hp, damage, speed)

    def __str__(self):
        return "SZ"
    

class FastZombie(Zombie):

    def __init__(self, x, y):
        hp = 50
        damage = 100
        speed = 1

        super().__init__(x, y, hp, damage, speed)

    def __str__(self):
        return f"FZ"
    

class Engine:

    def __init__(self) -> None:
        self.rnd = 0

    def run(self):
        global my_map

        my_map = Map(10, 10)
        # my_map.print_map()

        zombies_rounds = {
            20: [
                SlowZombie(
                    x=my_map.width - 1, 
                    y=random.randint(0, my_map.length - 1), 
                ),
                FastZombie(
                    x=my_map.width - 1, 
                    y=random.randint(0, my_map.length - 1), 
                )
            ]
        }

        while True:
            time.sleep(0.5)

            print(f"--------------------------{self.rnd}------------------------------")
            my_map.print_map()


            for row in my_map.board:
                for cell in row:
                    for obj in cell.contents:
                        if isinstance(obj, (SlowZombie, FastZombie)):
                            obj.move()

            # {
            #  'hassan': 'akbari',
            # }.get('ali', 'asghari')

            for zombie in zombies_rounds.get(self.rnd, []):
                # obj, x, y
                my_map.add_content(zombie, zombie.x, zombie.y)

            self.rnd += 1

            if self.rnd == 100:
                break



engine = Engine()
engine.run()