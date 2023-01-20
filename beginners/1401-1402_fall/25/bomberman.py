import threading
import keyboard
import random
import time
import os
from datetime import datetime


# global scope
is_game_over = False
board = None
bomberman = None
won = False

# constants
CELL_WIDTH = 7


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

    def burst(self):
        # TODO
        pass


class StoneCell(Cell):

    def __str__(self):
        return "|" * CELL_WIDTH


class WallCell(Cell):

    def __str__(self):
        return "#" * CELL_WIDTH


class PathCell(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
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

    def get_content(self, content_type):
        for content in self.__contents:
            if isinstance(content, content_type):
                return content
        return None

    def is_empty(self):
        return len(self.__contents) == 0

    def __str__(self):
        return " ".join([str(content) for content in self.__contents])


class DoorCell(Cell):

    def __str__(self):
        return "D"


class Map:

    def __init__(self, height, width, wall_count=20):
        self.height = height
        self.width = width
        self.board = []

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
            if candidate_cell.is_path:
                wall_cell = WallCell(x=random_x, y=random_y)
                self.board[random_y][random_x] = wall_cell
                wall_cnt += 1

    def get_cell(self, x, y):
        return self.board[y][x]

    def print_board(self):
        # os.system("cls")
        roof = "-" * ((CELL_WIDTH + 1) * self.width + 1)

        for row in self.board:
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

            directions_relative_path = [
                (1, 0), # right
                (-1, 0), # left
                (0, -1), # up
                (0, 1), # down
            ]

            for i in range(1, self.bomb_range + 1):
                
                cnt = 0
                while cnt < len(directions_relative_path):
                    relative_dir = directions_relative_path[cnt] 
                    relative_x = i * relative_dir[0]
                    relative_y = i * relative_dir[1]

                    if 0 <= relative_x < board.width and 0 <= relative_y < board.height:
                        cell = board.get_cell(x=relative_x, y=relative_y)
                        blockage = cell.burst()

                        if blockage:
                            directions_relative_path.remove(relative_dir)
                        else:
                            cnt += 1
                    else:
                        directions_relative_path.remove(relative_dir)
            
            cell = board.get_cell(self.x, self.y)
            cell.remove_contents(self)
            Bomb.CURRENT_BOMBS.remove(self)

    @classmethod
    def get_active_bombs(cls):
        return cls.CURRENT_BOMBS

    def __str__(self):
        return "B"


class Moveable:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        cell = board.get_cell(x=x, y=y)
        cell.add_contents(self)

    def __is_allowed(self, x, y):

        if not ((0 <= x < board.width) and (0 <= y < board.height)):
            return False

        candidate_cell = board.get_cell(x, y)

        if candidate_cell.is_stone or candidate_cell.is_wall:
            return False

        if candidate_cell.consist_of(Bomb):
            return False

        return True

    def __move(self, x, y):
        current_cell = board.get_cell(self.x, self.y)
        current_cell.remove_contents(self)

        self.x = x
        self.y = y

        next_cell = board.get_cell(self.x, self.y)
        next_cell.add_contents(self)

        if next_cell.consist_of(Bomberman if isinstance(self, Enemy) else Enemy):
            global is_game_over
            is_game_over = True

    def move(self, direction):
        # `lambda : print("Invalid directino")` dummy function used as default value 
        return {
            "right": lambda :  self.__is_allowed(x=self.x+1, y=self.y) and self.__move(x=self.x+1, y=self.y),
            "left": lambda :  self.__is_allowed(x=self.x-1, y=self.y) and self.__move(x=self.x-1, y=self.y),
            "up": lambda :  self.__is_allowed(x=self.x, y=self.y-1) and self.__move(x=self.x, y=self.y-1),
            "down": lambda :  self.__is_allowed(x=self.x, y=self.y+1) and self.__move(x=self.x, y=self.y+1),
        }.get(direction, lambda : print("Invalid directino"))()

    def die(self):
        cell = board.get_cell(x=self.x, y=self.y)
        cell.remove_contents(self)


class Enemy(Moveable):
    ENEMIES = []

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        Enemy.ENEMIES.append(self)

    @classmethod
    def get_enemies(cls):
        return cls.ENEMIES

    def move(self):
        super().move(random.choice(["right","left","up","down"]))

    def die(self):
        super().die()
        Enemy.ENEMIES.remove(self)

    def __str__(self):
        return "E"
        

class Bomberman(Moveable):

    def __init__(self, x, y, bomb_count=1, bomb_range=1):
        super().__init__(x=x, y=y)
        
        self.__bomb_count = bomb_count
        self.__bomb_range = bomb_range

    def plant_bomb(self):
        current_cell = board.get_cell(self.x, self.y)

        if current_cell.consist_of(Bomb):
            return

        active_bombs = Bomb.get_active_bombs()
        if len(active_bombs) < self.__bomb_count:
            Bomb(x=self.x, y=self.y, bomb_range=self.__bomb_range)

    def die(self):
        super().die()

        global is_game_over
        is_game_over = True

    def __str__(self):
        return "M"


class Engine:

    def __init__(self, enemy_count=5):
        self.enemy_count = enemy_count

    def enemy_listener(self):
        while not is_game_over:
            time.sleep(1)

            for enemey in Enemy.get_enemies():
                enemey.move()

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

    def instantiating_enemies(self):
        cnt = 0 
        while cnt < self.enemy_count:
            selected_x = random.randint(2, board.width - 1)
            selected_y = random.randint(2, board.height - 1)

            cell = board.get_cell(x=selected_x, y=selected_y)
            if cell.is_path:
                Enemy(x=selected_x, y=selected_y)
                cnt += 1

    def run(self):
        global board, bomberman

        board = Map(height=10, width=15)
        bomberman = Bomberman(x=0, y=0)

        # instantiating_enemies
        self.instantiating_enemies()

        keyboar_listener = threading.Thread(target=self.keyboard_listener)
        keyboar_listener.start()

        bomb_listener = threading.Thread(target=self.bomb_listener)
        bomb_listener.start()

        enemy_listener = threading.Thread(target=self.enemy_listener)
        enemy_listener.start()

        while not is_game_over:
            time.sleep(0.2)
            board.print_board()


engine = Engine()
engine.run()
