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
import random


CELL_WIDTH = 7
my_map = None
ball = None
is_game_over = False
snowboard = None


class SnowboardPartType:
    BODY = "body"
    HEAD = "head"
    TAIL = "tail"


class Direction:
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"


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

    def consist_of(self, content_type):
        for content in self.contents:
            if isinstance(content, content_type):
                return True

        return False

    def get_content(self, content_type):
        for content in self.contents:
            if isinstance(content, content_type):
                return content

        return None

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
        os.system("clear")
        roof = "-" * ((self.width * (CELL_WIDTH + 1)) + 1)

        # [[], [], []]
        for row in self.__board:
            # row: [Cell, Cell, Cell]
            print(roof)
            print("|" + "|".join([str(cell) for cell in row]) + "|")

        print(roof)


class SnowboardPart:
    
    def __init__(self, x, y, typ=SnowboardPartType.BODY):
        self.x = x
        self.y = y
        self.typ = typ

        cell = my_map.get_cell(x=x, y=y)
        cell.add_content(self)

    def __str__(self):
        shape = ""

        if self.typ == SnowboardPartType.BODY:
            shape =  "_"
        elif self.typ == SnowboardPartType.HEAD:
            shape = "\\"
        elif self.typ == SnowboardPartType.TAIL:
            shape =  "/"

        return shape * CELL_WIDTH


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

        self.__parts[0].typ = SnowboardPartType.HEAD
        self.__parts[-1].typ = SnowboardPartType.TAIL

    def __move_right(self):
        # [][][][][]
        if self.__parts[0].x < my_map.width - self.length:
            head_snowboard = self.__parts.pop(0)

            prev_cell = my_map.get_cell(x=head_snowboard.x, y=head_snowboard.y)
            prev_cell.remove_content(head_snowboard)

            head_snowboard.x += self.length
            head_snowboard.typ = SnowboardPartType.TAIL

            self.__parts[-1].typ = SnowboardPartType.BODY
            self.__parts[0].typ = SnowboardPartType.HEAD

            current_cell = my_map.get_cell(x=head_snowboard.x, y=head_snowboard.y)
            current_cell.add_content(head_snowboard)
            
            self.__parts.append(head_snowboard)

    def __move_down(self):
        if self.__parts[0].y < my_map.height - 1:
            for part in self.__parts:
                prev_cell = my_map.get_cell(x=part.x, y=part.y)
                prev_cell.remove_content(part)

                part.y += 1

                current_cell = my_map.get_cell(x=part.x, y=part.y)
                current_cell.add_content(part)
    
    def __move_up(self):
        if  Brick.MAX_Y + 1 < self.__parts[0].y:
            for part in self.__parts:
                prev_cell = my_map.get_cell(x=part.x, y=part.y)
                prev_cell.remove_content(part)

                part.y -= 1

                current_cell = my_map.get_cell(x=part.x, y=part.y)
                current_cell.add_content(part)
    
    def __move_left(self):
        if 0 < self.__parts[0].x:
            tail_snowboard = self.__parts.pop(self.length - 1)

            prev_cell = my_map.get_cell(x=tail_snowboard.x, y=tail_snowboard.y)
            prev_cell.remove_content(tail_snowboard)

            tail_snowboard.x -= self.length
            tail_snowboard.typ = SnowboardPartType.HEAD

            self.__parts[0].typ = SnowboardPartType.BODY
            self.__parts[-1].typ = SnowboardPartType.TAIL

            current_cell = my_map.get_cell(x=tail_snowboard.x, y=tail_snowboard.y)
            current_cell.add_content(tail_snowboard)
            
            self.__parts.insert(0, tail_snowboard)

    def move(self, direction):
        if direction == "right":
            self.__move_right()
        elif direction == "left":
            self.__move_left()
        elif direction == "up":
            self.__move_up()
        elif direction == "down":
            self.__move_down()


class Brick:
    BRICKS = []
    MAX_Y = 0

    def __init__(self, x, y, hp) -> None:
        self.x = x 
        self.y = y
        self.hp = hp

        Brick.BRICKS.append(self)

        cell = my_map.get_cell(x=self.x, y=self.y)
        cell.add_content(self)

        if self.y > Brick.MAX_Y:
            Brick.MAX_Y = self.y 

    @classmethod
    def get_bricks(cls):
        return cls.BRICKS

    def damage(self, power=1):
        self.hp -= power

        if self.hp <= 0:
            Brick.BRICKS.remove(self)
            cell = my_map.get_cell(x=self.x, y=self.y)
            cell.remove_content(self)

    def __str__(self) -> str:
        shape = ""

        if self.hp == 2:
            shape = "%"
        else:
            shape = "#"
        
        return shape.center(CELL_WIDTH)


class Ball:
    
    def __init__(self, x, y, power) -> None:
        self.x = x
        self.y = y
        self.power = power
        self.y_angle = -1
        self.x_angle = -1

        cell = my_map.get_cell(x=x, y=y)
        cell.add_content(self)

    def move(self):
        
        """
        -----------------------------------------------------------------------
        |      |      |      |      |$$$$$$|$$$$$$|$$$$$$|      |      |      |
        -----------------------------------------------------------------------
        |      |      |      |      |      |      |      |      |      |      |
        -----------------------------------------------------------------------
        |      |      |      |      |      |      |      |      |      |  *   |
        -----------------------------------------------------------------------
        |      |      |      |   *  |      |   *  |      |      |      |      |
        -----------------------------------------------------------------------
        |      |      |      |      |   *  |      |      |      |      |      |
        -----------------------------------------------------------------------
        |      |      |      |------|------|------|      |      |      |      |
        -----------------------------------------------------------------------
                                        x: 5
                                        y: 6
        RIGHT:
            UP:
                +x
                -y
            DOWN:
                -x
                +y

        LEFT:
            UP:
                -x
                -y
            DOWN:
                +x
                +y
        """
        next_x = self.x + self.x_angle 
        next_y = self.y + self.y_angle 

        if not (0 <= next_x < my_map.width):
            self.x_angle *= -1 
            return

        if next_y < 0:
            self.y_angle *= -1 
            return

        elif next_y >= my_map.height:
            global is_game_over
            is_game_over = True
            return 

        candidate_cell = my_map.get_cell(x=next_x, y=next_y)

        if candidate_cell.consist_of(SnowboardPart):
            self.y_angle *= -1
        
        elif candidate_cell.consist_of(Brick): 
            self.y_angle *= -1

            brick = candidate_cell.get_content(Brick)
            brick.damage(self.power)
        else:
            current_cell = my_map.get_cell(x=self.x, y=self.y)
            current_cell.remove_content(self)

            self.x = next_x
            self.y = next_y

            candidate_cell.add_content(self)

    def __str__(self) -> str:
        return "⚽"

class Engine:


    def handle_ball_movement(self):
        while not is_game_over:
            time.sleep(.5)
            ball.move()

    def handle_keyboard_action(self):
        while not is_game_over:
            key = keyboard.read_key()
            # press release
            # 
            if keyboard.is_pressed(key):
                if key in ["up", "down", "right", "left"]: 
                    snowboard.move(direction=key)

    def run(self):
        global my_map, snowboard, ball

        my_map = Map(height=10, width=15)
        snowboard = Snowboard(initial_x=5, initial_y=9, length=5)

        ball = Ball(x=5, y=5, power=1)

        keyboard_listener = threading.Thread(target=self.handle_keyboard_action)
        keyboard_listener.start()

        ball_listener = threading.Thread(target=self.handle_ball_movement)
        ball_listener.start()

        for y in range(2):
            for x in range(my_map.width):
                Brick(x=x, y=y, hp=1 if x % 2 == 0 else 2)

        while not is_game_over:
            time.sleep(0.1)
            my_map.print_board()

        print("GAME OVER ...")


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