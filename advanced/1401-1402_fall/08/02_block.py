"""
Ball
Brick
Cell
Map
SnowboardPart
Snowboard
Engine
"""

import keyboard
import threading
import time
import os


CELL_WIDTH = 7
my_map = None
snowboard = None

class Cell:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__contents = []

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def contents(self):
        return self.__contents

    def add_content(self, item):
        self.__contents.append(item)

    def remove_content(self, item):
        self.__contents.remove(item)

    def __str__(self):
        # contents: [Snowboard, Brick, Ball]
        #
        return " ".join([str(content) for content in self.__contents]).center(CELL_WIDTH)
        # return "Cell"


class Map:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        """
        [
            [Cell, Cell, Cell, Cell],
            [],
            [],
            [],
            [],
        ]
        """
        self.__board = [
            [Cell(x=x, y=y) for x in range(self.width)] for y in range(self.height)
        ]

        # self.__board = []
        # board: []
        # for y in range(self.height):
        #     row = []
        #     for x in range(self.width):
        #         cell = Cell(x=x, y=y)
        #         row.append(cell)
        #     # row: [Cell, Cell, Cell, Cell, Cell]
        #     self.__board.append(row)
        #     # board: [[Cell, Cell, Cell, Cell, Cell], [Cell, Cell, Cell, Cell, Cell], [Cell, Cell, Cell, Cell, Cell]]

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def get_cell(self, x, y):
        return self.__board[y][x]

    def print_board(self):
        """
        ------------------------------------
        |      |      |      |      |      |
        ------------------------------------
        |      |      |      |      |      |
        ------------------------------------
        |      |      |      |      |      |
        ------------------------------------
        |      |      |      |      |      |
        ------------------------------------
        |      |      |      |      |      |
        ------------------------------------
        |      |      |      |      |      |
        ------------------------------------
        (CELL_WIDTH * self.width) + (1 * self.width + 1)
        (self.width * (CELL_WIDTH + 1)) + 1
        """
        os.system("cls")
        roof = "-" * ((self.width * (CELL_WIDTH + 1)) + 1)

        # [[], [], []]
        for row in self.__board:
            # row: [Cell, Cell, Cell]
            print(roof)
            print("|" + "|".join([str(cell) for cell in row]) + "|")

        print(roof)


class SnowboardPart:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        cell = my_map.get_cell(x=x, y=y)
        cell.add_content(self)

    def __str__(self):
        return "_" * CELL_WIDTH


class Snowboard:

    def __init__(self, initial_x, initial_y, length):
        self.initial_x = initial_x 
        self.initial_y = initial_y 
        self.length = length
        """

            x: 4
            y: 10
            length: 5

            (4, 10), (5, 10), (6, 10), (7, 10), (8, 10)
            9 14
        """
        self.__parts = [
            SnowboardPart(x=x, y=initial_y) for x in range(initial_x, initial_x +  length)
        ]

    def __move_right(self):
        # [][][][][]
        if self.__parts[0].x < my_map.width - self.length - 1:
            head_snowboard = self.__parts.pop(0)

            prev_cell = my_map.get_cell(x=head_snowboard.x, y=head_snowboard.y)
            prev_cell.remove_content(head_snowboard)

            head_snowboard.x += self.length

            current_cell = my_map.get_cell(x=head_snowboard.x, y=head_snowboard.y)
            current_cell.add_content(head_snowboard)
            
            self.__parts.append(head_snowboard)

    def __move_down(self):
        pass
    
    def __move_up(self):
        pass
    
    def __move_left(self):
        pass

    def move(self, direction):
        if direction == "right":
            self.__move_right()


class Engine:

    def handle_keyboard_action(self):

        while True:
            key = keyboard.read_key()
            # press release
            # 
            if keyboard.is_pressed(key):
                if key in ["up", "down", "right", "left"]: 
                    snowboard.move(direction=key)

    def run(self):
        global my_map, snowboard

        my_map = Map(height=10, width=15)
        snowboard = Snowboard(initial_x=5, initial_y=9, length=5)

        keyboard_listener = threading.Thread(target=self.handle_keyboard_action)
        keyboard_listener.start()

        while True:
            time.sleep(0.5)
            my_map.print_board()


engine = Engine()
engine.run()

# print("S B".center(CELL_WIDTH))


# cell = Cell(x=10, y=10)
# str(cell)
# print(cell)
# str(list)
# my_list = [cell]
# print(my_list)
# print([str(item) for item in my_list])
