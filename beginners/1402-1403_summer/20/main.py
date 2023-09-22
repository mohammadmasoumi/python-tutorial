
import random
import keyboard

"""
Terminal
pip install keyboard

Connection refuse -> filter 
"""
"""
Objects:
    - human
        : hp
        : move
        - fighter
            : damage
            : jump
            : fight
        - enemy
            : move
    - map
    - cell
        - wall
        - path
    - box
    - card skill
"""

# constant
CELL_WIDTH = 11

"""
------------------------------------
|      |      |      |      |      |
------------------------------------
|||||||||||||||      ||||||||      |
------------------------------------
|      |||||||||||||||      |      |
------------------------------------
|      |      |      |      |      |
------------------------------------
"""


class Cell:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Wall(Cell):

    def __str__(self):
        return "|" * CELL_WIDTH


class Path(Cell):

    def __init__(self, x, y):
        self.__contents = []
        super().__init__(x, y)

    @property
    def content(self):
        return self.__contents

    def add_content(self, content):
        self.__contents.append(content)

    def remove_content(self, content):
        self.__contents.remove(content)

    def __str__(self):
        # H-E
        # return ""
        return "-".join(map(str, self.__contents))


# wall = Wall(x=1, y=1)
# print(wall)


class Map:
    """
    [
         col:0 col:1 col:2 col:3 col:4 col:5
        [Cell, Cell, Cell, Cell, Cell, Cell], row: 0
        [Cell, Cell, Cell, Cell, Cell, Cell], row: 1
        [Cell, Wall, Cell, Cell, Cell, Cell], row: 2
        [Cell, Cell, Cell, Cell, Cell, Cell], row: 3
        [Cell, Cell, Cell, Cell, Cell, Cell], row: 4
        [Cell, Cell, Cell, Cell, Cell, Cell], row: 5
    ]
    """

    def __init__(self, height, width, number_of_walls):
        self.__height = height
        self.__width = width
        self.__number_of_walls = number_of_walls
        self.__board = [
            [Path(x=x, y=y) for x in range(self.__width)] for y in range(self.__height)
        ]
        """
        [[i + j for j in range(20)] for i in range(10)]
        [i + 2 for i in range(10)]
        """
        wall_cnt = 0
        while wall_cnt < self.__number_of_walls:
            x = random.randint(1, self.__width-1)
            y = random.randint(1, self.__height-1)

            candidate_cell = self.__board[y][x]
            if isinstance(candidate_cell, Path):
                # row: self.__board[y]
                # col: self.__board[y][x]
                self.__board[y][x] = Wall(x=x, y=y)
                wall_cnt += 1

    @property
    def board(self):
        return self.__board

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def print_map(self):
        """
        self.__board
        [
            col:0 col:1 col:2 col:3 col:4 col:5
            [Path, Path, Path, Path, Path, Path], row: 0
            [Path, Path, Path, Path, Path, Path], row: 1
            [Path, Path, Wall, Path, Wall, Path], row: 2
            [Path, Path, Wall, Path, Path, Path], row: 3
            [Path, Path, Path, Path, Path, Path], row: 4
            [Path, Path, Wall, Path, Path, Path], row: 5
        ]
                       "|"               last pipe

        ------------------------------------
        |      |      |      |      |      |
        ------------------------------------
        |||||||||||||||      ||||||||      |
        ------------------------------------
        |      |||||||||||||||      |      |
        ------------------------------------
        |      |      |      |      |      |
        ------------------------------------
        """
        ceil_width = (self.__width * (1 + CELL_WIDTH)) + 1
        for row in self.__board:
            # row: [Path, Path, Path, Wall, Path, Path]
            # "[Path, Path, Path, Path, Path, Path]"
            """
            [<__main__.Path object at 0x000002267FC8E890>, <__main__.Path object at 0x000002267FC8E9D0>, <__main__.Path object at 0x000002267FC8EA50>, <__main__.Path object at 0x000002267FC8EAD0>, <__main__.Wall object at 0x000002267FC8DB50>, <__main__.Path object at 0x000002267FC8EB90>, <__main__.Path object at 0x000002267FC8EC90>, <__main__.Path object at 0x000002267FC8ED10>, <__main__.Path object at 0x000002267FC8ED90>, <__main__.Path object at 0x000002267FC8EBD0>]
            [|<|_|_|m|a|i|n|_|_|.|P|a|t|h| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|8|9|0|>|,| |<|_|_|m|a|i|n|_|_|.|P|a|t|h| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|9|D|0|>|,| |<|_|_|m|a|i|n|_|_|.|W|a|l|l| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|B|5|0|>|,| |<|_|_|m|a|i|n|_|_|.|P|a|t|h| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|A|D|0|>|,| |<|_|_|m|a|i|n|_|_|.|W|a|l|l| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|7|D|0|>|,| |<|_|_|m|a|i|n|_|_|.|P|a|t|h| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|B|9|0|>|,| |<|_|_|m|a|i|n|_|_|.|P|a|t|h| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|C|9|0|>|,| |<|_|_|m|a|i|n|_|_|.|P|a|t|h| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|D|1|0|>|,| |<|_|_|m|a|i|n|_|_|.|P|a|t|h| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|D|9|0|>|,| |<|_|_|m|a|i|n|_|_|.|P|a|t|h| |o|b|j|e|c|t| |a|t| |0|x|0|0|0|0|0|1|F|C|F|7|6|9|E|B|D|0|>|]|
            """
            print("-" * ceil_width)
            print("|" + "|".join(map(lambda c: str(c).center(CELL_WIDTH), row)) + "|")

        print("-" * ceil_width)

    def __str__(self):
        board = ""
        ceil_width = (self.__width * (1 + CELL_WIDTH)) + 1
        for row in self.__board:
            board += "-" * ceil_width + "\n"
            board += "|" + "|".join(map(lambda c: str(c).center(CELL_WIDTH), row)) + "|\n"

        return board + "-" * ceil_width + "\n"


class Human:
    
    def __init__(self, x, y, hp):
        self.__x = x
        self.__y = y
        self.__hp = hp

        # my_map.board[y][x]: Path
        my_map.board[y][x].add_content(self)

    def __move(self, new_x, new_y):
        if 0 <= new_x < my_map.width and 0 <= new_y < my_map.height:
            current_cell = my_map.board[self.__y][self.__x]
            candidate_cell = my_map.board[new_y][new_x]
            if isinstance(candidate_cell, Path):
                # remove hero from previous cell
                current_cell.remove_content(self)
                candidate_cell.add_content(self)
                self.__y = new_y
                self.__x = new_x

    def move(self, direction):
        # down
        if direction == "down":
            self.__move(self.__x, self.__y + 1)
        elif direction == "up":
            self.__move(self.__x, self.__y - 1)
        elif direction == "right":
            self.__move(self.__x + 1, self.__y)
        elif direction == "left":
            self.__move(self.__x - 1, self.__y)

class Hero(Human):
    def __str__(self):
        return "H"

class Enemy(Human):
    def __str__(self):
        return "E"

# print([[i + j for j in range(5)] for i in range(5)])
my_map=Map(height=5, width=10, number_of_walls=5)
hero = Hero(x=0, y=0, hp=100)
# board.print_map()
print(my_map)

while True:

    action_key = keyboard.read_key()

    if keyboard.is_pressed(action_key):
        # if action_key == "space":
        #     bomberman.plant_bomb()

        if action_key in ["down", "up", "right", "left"]:
            print(action_key)
            hero.move(direction=action_key)

        print(my_map)


# class Engine:
#     def __init__(self, height, width, number_of_wall):


