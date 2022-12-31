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
import threading
import keyboard
import random
import time
import os
from datetime import datetime, timedelta
CELL_WIDTH = 7

"""
x 
y 
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

                            Cell
        ContentHolderCell  DoorCell  BlockCell
    PathCell    WallCell
"""


# global scope
is_game_over = False
board = None
bomberman = None
won = False

# class Cell1:
#     def __init__(self, x, y, typ):
#         self.x = x
#         self.y = y
#         self.typ = typ


class SkillCard:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class BombCountCard(SkillCard):

    def __str__(self):
        return "C"


class BombExpolisionRangeCard(SkillCard):

    def __str__(self):
        return "R"


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def is_path(self):
        return isinstance(self, PathCell)

    @property
    def is_door(self):
        return isinstance(self, DoorCell)

    @property
    def is_stone(self):
        return isinstance(self, StoneCell)

    @property
    def is_wall(self):
        return isinstance(self, WallCell)


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

    def __init__(self, height, width, wall_count=20):

        self.height = height
        self.width = width
        self.board = []

        # for y in range(self.height):
        # row = []
        # for x in range(self.width):
        #     if x % 2 and y % 2:
        #         stone_cell = StoneCell(x=x, y=y)
        #         row.append(stone_cell)
        #     else:
        #         path_cell = PathCell(x=x, y=y)
        #         row.append(path_cell)

        # row = [StoneCell(x=x, y=y) if x % 2 and y %
        #        2 else PathCell(x=x, y=y) for x in range(self.width)]

        # self.board.append(row)
        # self.board.append(
        #     [StoneCell(x=x, y=y) if x % 2 and y % 2 else PathCell(x=x, y=y) for x in range(self.width)]
        # )

        self.board = [
            [StoneCell(x=x, y=y) if x % 2 and y % 2 else PathCell(x=x, y=y)
             for x in range(self.width)]
            for y in range(self.height)
        ]

        wall_cnt = 0

        while wall_cnt < wall_count:
            random_x = random.randint(2, self.width - 1)
            random_y = random.randint(2, self.height - 1)

            candidate_cell = self.board[random_y][random_x]

            # a = [12, 13 ,14]
            # a[2] = 15
            # a = [[1, 2], [3, 4]]
            # a[1][1] = 5

            # if isinstance(candidate_cell, PathCell):
            if candidate_cell.is_path:
                wall_cell = WallCell(x=random_x, y=random_y)
                # is_path = wall_cell
                self.board[random_y][random_x] = wall_cell
                wall_cnt += 1

    def get_cell(self, x, y):
        return self.board[y][x]

    def print_board(self):
        os.system("cls")
        roof = "-" * ((CELL_WIDTH + 1) * self.width + 1)

        for row in self.board:
            # [Cell, Cell, Cell]
            print(f"{roof}")
            print("|" + "|".join([str(cell).center(CELL_WIDTH)
                                  for cell in row]) + "|")

        print(f"{roof}")


class Bomb:
    CURRENT_BOMBS = []
    TIMER = 2

    def __init__(self, x, y, bomb_range):
        self.x = x
        self.y = y
        self.created_time = datetime.utcnow()
        self.bomb_range = bomb_range

        cell = board.get_cell(x=x, y=y)
        cell.add_contents(self)

        Bomb.CURRENT_BOMBS.append(self)

    def __should_exploid(self):
        return (datetime.utcnow() - self.created_time).seconds > self.TIMER

    def exploid(self):
        if self.__should_exploid():
            # ToDo
            
            print("Banggggggggggggggggggggggggg")
            cell = board.get_cell(self.x, self.y)
            cell.remove_contents(self)
            Bomb.CURRENT_BOMBS.remove(self)

    @classmethod
    def get_active_bombs(cls):
        return cls.CURRENT_BOMBS

    def __str__(self):
        return "B"


class Enemy:
    pass


class Bomberman:

    def __init__(self, x, y, bomb_count=1, bomb_range=1):
        self.x = x
        self.y = y

        self.__bomb_count = bomb_count
        self.__bomb_range = bomb_range

        cell = board.get_cell(x=x, y=y)
        cell.add_contents(self)

    def __is_allowed_to_move(self, selected_x, selected_y):

        if not ((0 <= selected_x < board.width) and (0 <= selected_y < board.height)):
            return False

        candidate_cell = board.get_cell(selected_x, selected_y)

        if candidate_cell.is_stone or candidate_cell.is_wall:
            return False

        if candidate_cell.consist_of(Bomb):
            return False

        return True

    def __move(self, selected_x, selected_y):
        if self.__is_allowed_to_move(selected_x=selected_x, selected_y=selected_y):
            current_cell = board.get_cell(self.x, self.y)
            current_cell.remove_contents(self)

            self.x = selected_x
            self.y = selected_y

            next_cell = board.get_cell(self.x, self.y)
            next_cell.add_contents(self)

            if next_cell.consist_of(Enemy):
                global is_game_over
                is_game_over = True

    def __move_right(self):
        selected_x = self.x + 1
        selected_y = self.y

        self.__move(selected_x=selected_x, selected_y=selected_y)

    def __move_left(self):
        selected_x = self.x - 1
        selected_y = self.y

        self.__move(selected_x=selected_x, selected_y=selected_y)

    def __move_up(self):
        selected_x = self.x
        selected_y = self.y - 1

        self.__move(selected_x=selected_x, selected_y=selected_y)

    def __move_down(self):
        selected_x = self.x
        selected_y = self.y + 1

        self.__move(selected_x=selected_x, selected_y=selected_y)

    def move(self, direction):
        DIRECTION_2_HANDLERS = {
            "right": self.__move_right,
            "left": self.__move_left,
            "up": self.__move_up,
            "down": self.__move_down,
        }
        # handler = self.__move_right
        # self.__move_right()
        # handler()
        handler = DIRECTION_2_HANDLERS.get(direction)
        handler() if handler else None

    def plant_bomb(self):
        current_cell = board.get_cell(self.x, self.y)

        if current_cell.consist_of(Bomb):
            return

        active_bombs = Bomb.get_active_bombs()
        if len(active_bombs) < self.__bomb_count:
            Bomb(x=self.x, y=self.y, bomb_range=self.__bomb_range)

    def __str__(self):
        return "M"


class Engine:

    def __init__(self):
        pass

    def bomb_listener(self):
        while not is_game_over:
            time.sleep(0.1)
            for bomb in Bomb.CURRENT_BOMBS:
                bomb.exploid()

    def keyboard_listener(self):
        # constant
        MOVEMENT_KEYS = ["up", "down", "right", "left"]
        while not is_game_over:
            # block
            action_key = keyboard.read_key()

            if keyboard.is_pressed(action_key):

                if action_key in MOVEMENT_KEYS:
                    # move bomberman
                    bomberman.move(action_key)

                elif action_key == "space":
                    bomberman.plant_bomb()

    def run(self):
        global board, bomberman

        board = Map(height=10, width=15)
        bomberman = Bomberman(x=0, y=0)

        keyboar_listener = threading.Thread(target=self.keyboard_listener)
        keyboar_listener.start()

        bomb_listener = threading.Thread(target=self.bomb_listener)
        bomb_listener.start()

        while not is_game_over:
            time.sleep(0.2)
            board.print_board()


engine = Engine()
engine.run()
