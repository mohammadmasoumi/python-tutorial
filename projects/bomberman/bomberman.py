"""
Snake Game

In order to run game please run below commands in terminal

```
pip install keyboard
```

Have fun!
"""

import os
import time
import threading
import keyboard
import random
from datetime import datetime, timedelta

game_over = False
won = False
board = None
bomberman = None
CELL_WIDTH = 11


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class CellType:
    BLOCK = "block"
    WALL = "wall"
    PATH = "path"
    DOOR = "door"


class Destroyable:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    def die(self):
        global board

        cell = board.get_cell(self.x, self.y)
        cell.remove_contents(self)


class Skill(Destroyable):

    def __init__(self, x, y):
        super().__init__(x, y)


class BombCountSkill(Skill):
    BOMB_COUNT_INC = 1

    def __str__(self):
        return "C"


class BombCastRangeSkill(Skill):
    BOMB_CAST_RANGE_INC = 1

    def __str__(self):
        "R"


class Cell:
    WALL_COUNT = 0

    def __init__(self, x, y, typ):
        self.__x = x
        self.__y = y
        self.__type = typ
        self.__contents = []

        if self.is_wall:
            Cell.WALL_COUNT += 1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def typ(self):
        return self.__type

    @typ.setter
    def typ(self, value):
        self.__type = value

        if self.is_wall:
            Cell.WALL_COUNT += 1

    @property
    def contents(self):
        return self.__contents

    def get_content(self, content_type):
        for content in self.contents:
            if isinstance(content, content_type):
                return content
        return None

    def add_contents(self, element):
        return self.contents.append(element)

    def remove_contents(self, element):
        return self.contents.remove(element)

    def consist_of(self, content_type):
        for content in self.contents:
            if isinstance(content, content_type):
                return True
        return False

    @property
    def is_block(self):
        return self.__type == CellType.BLOCK

    @property
    def is_wall(self):
        return self.__type == CellType.WALL

    @property
    def is_path(self):
        return self.__type == CellType.PATH

    @property
    def is_door(self):
        return self.__type == CellType.DOOR

    @property
    def is_empty(self):
        return len(self.__contents) == 0

    def on_burst(self):
        if not self.is_wall:
            return

        if Cell.WALL_COUNT == 1:
            self.__type = CellType.DOOR
        else:
            self.__type = CellType.PATH
            random_num = random.randint(1, 100)

            ability = None

            if random_num <= 10:
                ability = BombCountSkill(self.x, self.y)

            elif random_num <= 20:
                ability = BombCastRangeSkill(self.x, self.y)

            self.add_contents(ability) if ability else None

        Cell.WALL_COUNT -= 1

    def __str__(self):
        if self.is_path:
            return " ".join([str(content) for content in self.contents])
        elif self.is_wall:
            return "#" * CELL_WIDTH
        elif self.is_block:
            return "|" * CELL_WIDTH
        elif self.is_door:
            return "D"


class Map:

    def __init__(self, height, width, wall_count=20):
        self.__height = height
        self.__width = width
        self.__board = [
            [
                Cell(
                    x=x, y=y,
                    typ=CellType.PATH if (y % 2 == 0) or (x % 2 == 0) else CellType.BLOCK) for x in range(self.__width)
            ]
            for y in range(self.__height)
        ]

        wall_cnt = 0
        while wall_cnt < wall_count:
            random_x = random.randint(1, self.__width - 1)
            random_y = random.randint(1, self.__height - 1)

            cell: Cell = self.get_cell(random_x, random_y)
            if cell.is_path and not cell.consist_of(Bomberman):
                cell.typ = CellType.WALL

                wall_cnt += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def get_cell(self, x, y):
        return self.__board[y][x]

    def print_board(self):
        os.system("clear")

        board_str = ""

        roof = "-" * ((CELL_WIDTH + 1) * self.__width + 1)
        board_str += f"{roof}\n"

        for row in self.__board:
            board_str += f"{roof}\n"
            board_str += Style.CYAN + "|" + "|".join([str(cell).center(CELL_WIDTH) for cell in row]) + "|\n"

        board_str += f"{roof}\n"

        print(board_str)


class Bomb:
    BOMBS = []
    BOMB_TIMER = 1

    def __init__(self, x, y, cast_range):
        self.__x = x
        self.__y = y
        self.__timer = datetime.utcnow()
        self.__cast_range = cast_range

        global board
        cell = board.get_cell(x, y)
        cell.add_contents(self)

        Bomb.BOMBS.append(self)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def cast_range(self):
        return self.__cast_range

    @classmethod
    def get_total_bombs(cls):
        return cls.BOMBS

    @classmethod
    def burst_all(cls):
        for bomb in cls.BOMBS:
            bomb.burst()

    def __burst_and_block(self, selected_x, selected_y):
        global board
        cell: Cell = board.get_cell(selected_x, selected_y)

        if cell.is_door or cell.is_block:
            return True
        elif cell.is_wall:
            cell.on_burst()
            return True
        else:
            # print(f"content: {cell.contents}")
            for content in cell.contents:
                content.die() if hasattr(content, "die") else None

        return False

    def burst(self):
        global board

        directions = [
            (1, 0),  # right
            (0, 1),  # down
            (-1, 0),  # left
            (0, -1)  # up
        ]

        duration = (datetime.utcnow() - self.__timer).seconds

        if duration >= 5:
            # burst current cell
            self.__burst_and_block(self.__x, self.__y)

            for rng in range(1, self.__cast_range + 1):

                cnt = 0
                while cnt < len(directions):
                    candidate_direction = directions[cnt]
                    candidate_x = self.__x + (rng * candidate_direction[0])
                    candidate_y = self.__y + (rng * candidate_direction[1])

                    if 0 <= candidate_x < board.width and 0 <= candidate_y < board.height:
                        blockage = self.__burst_and_block(candidate_x, candidate_y)
                        if blockage:
                            directions.remove(candidate_direction)
                        else:
                            cnt += 1
                    else:
                        directions.remove(candidate_direction)

            cell: Cell = board.get_cell(self.__x, self.__y)
            cell.remove_contents(self)
            Bomb.BOMBS.remove(self)

    def __str__(self):
        return "B"


class Bomberman(Destroyable):

    def __init__(self, x, y, initial_bomb_count=1, initial_bomb_cast_range=1):
        super().__init__(x, y)

        self.__bomb_count = initial_bomb_count
        self.__bomb_cast_range = initial_bomb_cast_range

        global board
        cell: Cell = board.get_cell(x, y)
        cell.add_contents(self)

    @property
    def bomb_count(self):
        return self.__bomb_count

    @property
    def bomb_cast_range(self):
        return self.__bomb_cast_range

    @staticmethod
    def __validate_movement(selected_x, selected_y):
        global board

        # 1. check index range
        if not (0 <= selected_x < board.width and 0 <= selected_y < board.height):
            return False

        cell: Cell = board.get_cell(x=selected_x, y=selected_y)
        if not cell.is_path:
            return False

        if cell.consist_of(Bomb):
            return False

        return True

    def __move(self, selected_x, selected_y):
        global board

        current_cell: Cell = board.get_cell(x=self.x, y=self.y)
        current_cell.remove_contents(self)

        self.x = selected_x
        self.y = selected_y

        new_cell: Cell = board.get_cell(x=self.x, y=self.y)
        new_cell.add_contents(self)

        if new_cell.is_door:
            global won
            won = True

        elif new_cell.consist_of(Enemy):
            global game_over
            game_over = True

        elif new_cell.consist_of(BombCountSkill):
            skill: BombCountSkill = new_cell.get_content(BombCountSkill)
            self.__bomb_count += skill.BOMB_COUNT_INC
            new_cell.remove_contents(skill)

        elif new_cell.consist_of(BombCastRangeSkill):
            skill: BombCastRangeSkill = new_cell.get_content(BombCastRangeSkill)
            self.__bomb_cast_range += skill.BOMB_CAST_RANGE_INC
            new_cell.remove_contents(skill)

    def move(self, direction):
        MOVEMENT__HANDLERS = {
            "right": lambda: self.__validate_movement(self.x + 1, self.y) and self.__move(self.x + 1, self.y),
            "left": lambda: self.__validate_movement(self.x - 1, self.y) and self.__move(self.x - 1, self.y),
            "down": lambda: self.__validate_movement(self.x, self.y + 1) and self.__move(self.x, self.y + 1),
            "up": lambda: self.__validate_movement(self.x, self.y - 1) and self.__move(self.x, self.y - 1)
        }

        handler = MOVEMENT__HANDLERS.get(direction)
        handler() if handler else None

    def die(self):
        super().die()

        global game_over, board
        game_over = True

    def plant_bomb(self):
        if len(Bomb.get_total_bombs()) >= self.__bomb_count:
            return

        Bomb(x=self.x, y=self.y, cast_range=self.__bomb_cast_range)

    def __str__(self):
        return "M"


class Enemy(Destroyable):
    ENEMIES = []

    def __init__(self, x, y):
        super().__init__(x, y)

        global board
        cell = board.get_cell(x=x, y=y)
        cell.add_contents(self)

        Enemy.ENEMIES.append(self)

    @classmethod
    def get_all_enemies(cls):
        return cls.ENEMIES

    @staticmethod
    def __validate_movement(selected_x, selected_y):
        global board

        # 1. check index range
        if not (0 <= selected_x < board.width and 0 <= selected_y < board.height):
            return False

        cell: Cell = board.get_cell(x=selected_x, y=selected_y)
        if not cell.is_path:
            return False

        return True

    def __move(self, selected_x, selected_y):
        global board

        current_cell: Cell = board.get_cell(x=self.x, y=self.y)
        current_cell.remove_contents(self)

        self.x = selected_x
        self.y = selected_y

        new_cell: Cell = board.get_cell(x=self.x, y=self.y)
        new_cell.add_contents(self)

        if new_cell.consist_of(Bomberman):
            global game_over
            game_over = True

    def move(self):
        MOVEMENT__HANDLERS = {
            1: lambda: self.__validate_movement(self.x + 1, self.y) and self.__move(self.x + 1, self.y),
            2: lambda: self.__validate_movement(self.x - 1, self.y) and self.__move(self.x - 1, self.y),
            3: lambda: self.__validate_movement(self.x, self.y + 1) and self.__move(self.x, self.y + 1),
            4: lambda: self.__validate_movement(self.x, self.y - 1) and self.__move(self.x, self.y - 1)
        }
        handler = MOVEMENT__HANDLERS.get(random.randint(1, 4))
        handler() if handler else None

    def die(self):
        super().die()
        Enemy.ENEMIES.remove(self)

    def __str__(self):
        return "E"


class Engine:

    def __init__(self, enemies_count=3):
        self.__enemies_count = enemies_count

    def keyboard_listener(self):
        global bomberman, game_over

        while True:
            if game_over:
                break

            action_key = keyboard.read_key()

            if keyboard.is_pressed(action_key):
                if action_key == "space":
                    bomberman.plant_bomb()

                if action_key in ["down", "up", "right", "left"]:
                    bomberman.move(direction=action_key)

    def bomb_listener(self):
        while True:
            if game_over:
                break

            time.sleep(0.5)
            Bomb.burst_all()

    def enemy_listener(self):
        while True:
            if game_over:
                break

            time.sleep(1)
            for enemy in Enemy.get_all_enemies():
                enemy.move()

    def run(self):
        global board, bomberman, game_over

        board = Map(height=10, width=15)
        bomberman = Bomberman(x=0, y=0)

        cnt = 0
        while cnt < self.__enemies_count:
            random_x = random.randint(3, board.width - 1)
            random_y = random.randint(3, board.height - 1)
            cell: Cell = board.get_cell(x=random_x, y=random_y)

            if cell.is_path:
                Enemy(x=random_x, y=random_y)
                cnt += 1

        board_listener = threading.Thread(target=self.keyboard_listener)
        board_listener.start()

        bomb_listener = threading.Thread(target=self.bomb_listener)
        bomb_listener.start()

        enemy_listener = threading.Thread(target=self.enemy_listener)
        enemy_listener.start()

        while True:
            if game_over:
                print("GameOver!")
                exit(0)

            time.sleep(0.1)
            board.print_board()


if __name__ == "__main__":
    engine = Engine()
    engine.run()
