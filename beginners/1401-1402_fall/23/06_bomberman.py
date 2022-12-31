"""

Cell
    Stone
    Wall
    Door
    Path


Map
Bomb
Bomberman
Enemy

Skill
    BombCountCard
    BombExpolisionRangeCard
"""
CELL_WIDTH = 7

"""
---------------------------------------------------------
|   M   |       |       |       |#######|       |       |
---------------------------------------------------------
|       |||||||||       |||||||||       |||||||||       |
---------------------------------------------------------
|       |       |       |       |#######|       |       |
---------------------------------------------------------
|       |||||||||#######|||||||||       |||||||||       |
---------------------------------------------------------
|       |       |#######|       |       |       |       |
---------------------------------------------------------
|       |||||||||       |||||||||#######|||||||||       |
---------------------------------------------------------
|       |       |       |#######|       |       |       |
---------------------------------------------------------
"""
import os
import time
import random
import keyboard
import threading

is_game_over = False
board = None
won = False


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def is_stone(self):
        return isinstance(self, StoneCell)

    @property
    def is_wall(self):
        return isinstance(self, WallCell)

    @property
    def is_door(self):
        return isinstance(self, DoorCell)

    @property
    def is_path(self):
        return isinstance(self, PathCell)


class StoneCell(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__typ = "stone"

    def __str__(self):
        return "|" * CELL_WIDTH


class WallCell(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__typ = "wall"

    def __str__(self):
        return "#" * CELL_WIDTH


class PathCell(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__typ = "path"
        self.__contents = []

    @property
    def contents(self):
        return self.__contents

    def add_contents(self, content):
        self.__contents.append(content)

    def remove_contents(self, content):
        self.__contents.remove(content)

    def consist_of(self, content_type):
        for content in self.__contents:
            if isinstance(content, content_type):
                return True
        return False

    def is_empty(self):
        return len(self.__contents) == 0

    def __str__(self):
        # contents: [Bomberman, Bomb, Enemy]
        # print(contents)
        # [Bomberman at x0000, Bomb at x8000, Enemy at x2000]
        # [str(content) for content in self.__contents]
        # ["M", "B", "E"]
        # " ".join(["M", "B", "E"])
        # "M B E"
        return " ".join([str(content) for content in self.__contents])


class DoorCell(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__typ = "door"

    def __str__(self):
        return "D"


class Map:

    def __init__(self, height, width, number_of_walls=20):

        self.height = height
        self.width = width
        self.number_of_walls = number_of_walls
        self.board = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                if y % 2 and x % 2:
                    # stone cell
                    stone = StoneCell(x=x, y=y)
                    # self.board[y][x] = stone
                    row.append(stone)

                else:
                    # path cell
                    path = PathCell(x=x, y=y)
                    # self.board[y][x] = path
                    row.append(path)

            self.board.append(row)


        wall_cnt = 0
        while wall_cnt < number_of_walls:
            random_x = random.randint(2, self.width - 1)
            random_y = random.randint(2, self.height - 1)

            selected_cell: Cell = self.board[random_y][random_x]
            if selected_cell.is_path:
                wall_cell = WallCell(x=random_x, y=random_y)
                self.board[random_y][random_x] = wall_cell
                wall_cnt += 1

    def get_cell(self, x, y):
        return self.board[y][x]

    def print_board(self):
        # os.system("cls")

        board_str = ""
        roof = "-" * ((CELL_WIDTH + 1) * self.width + 1)
        board_str += f"{roof}\n"

        for row in self.board:
            board_str += f"{roof}\n"
            board_str += "|" + "|".join([str(cell).center(CELL_WIDTH) for cell in row]) + "|\n"

        board_str += f"{roof}\n"

        print(board_str)


class Engine:

    def __init__(self):
        pass

    def run(self):
        global board

        board = Map(height=10, width=15)

        while not is_game_over:
            board.print_board()
            time.sleep(0.5)



engine = Engine()
engine.run()





