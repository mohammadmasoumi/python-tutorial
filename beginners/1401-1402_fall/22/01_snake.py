
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
import keyboard
import random
import threading

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


GAME_OVER_TEXT = """
                Game OVER!
                    \                             .       .
                    \                           / `.   .' " 
                    \                  .---.  <    > <    >  .---.
                    \                 |    \  \ - ~ ~ - /  /    |
                            _____          ..-~             ~-..-~
                            |     |   \~~~\.'                    `./~~~/
                        ---------   \__/                        \__/
                        .'  O    \     /               /       \  " 
                        (_____,    `._.'               |         }  \/~~~/
                        `----.          /       }     |        /    \__/
                                `-.      |       /      |       /      `. ,~~|
                                    ~-.__|      /_ - ~ ^|      /- _      `..-'   
                                        |     /        |     /     ~-.     `-. _  _  _
                                        |_____|        |_____|         ~ - . _ _ _ _ _>

                """
class Apple:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def plant(self):
        board.add_content(self.__x, self.__y, self)

    def __str__(self):
        return "A"  # "🍎"


class SnakePart:

    def __init__(self, x, y, next_part=None, prev_part=None):
        self.__x = x
        self.__y = y
        self.__next_part = next_part
        self.__prev_part = prev_part

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def next_part(self):
        return self.__next_part

    @property
    def prev_part(self):
        return self.__prev_part

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @next_part.setter
    def next_part(self, value):
        self.__next_part = value

    @prev_part.setter
    def prev_part(self, value):
        self.__prev_part = value

    def __str__(self):
        return '*'

class Snake:

    def __init__(self, h_initial_x, h_initial_y, t_initial_x, t_initial_y, current_direction):
        head = SnakePart(h_initial_x, h_initial_y)
        tail = SnakePart(t_initial_x, t_initial_y, next_part=head)

        head.prev_part = tail

        self.__head = head
        self.__tail = tail

        board.add_content(head.x, head.y, head)
        board.add_content(tail.x, tail.y, tail)

        self.__current_direction = current_direction

        self.DIRECTION_2_HANDLERS = {
            "right": lambda : self.__move(self.__head.x + 1, self.__head.y),
            "left": lambda: self.__move(self.__head.x - 1, self.__head.y),
            "up": lambda: self.__move(self.__head.x, self.__head.y - 1),
            "down": lambda: self.__move(self.__head.x, self.__head.y + 1),
        }

        self.NOT_ALLOWED_2_MOVE = {
            "right": "left",
            "left": "right",
            "up": "down",
            "down": "up", 
        }
    
    @property
    def current_direction(self):
        return self.__current_direction

    def __grow(self, selected_x, selected_y):
        new_head = SnakePart(
            x=selected_x,
            y=selected_y,
            prev_part=self.__head,
        )
        current_head = self.__head
        current_head.next_part = new_head

        self.__head = new_head
        board.add_content(self.__head.x, self.__head.y, self.__head)

    def __is_gameover(self, selected_x, selected_y):
        is_in_range = (0 <= selected_x < board.width) and (
            0 <= selected_y < board.height)
        
        hit_itself = board.consist_of(
            selected_x, selected_y, SnakePart) if is_in_range else False

        if not is_in_range or hit_itself:
            global game_is_over
            game_is_over = True
            return True

        return False

    def __move(self, selected_x, selected_y):
        if self.__is_gameover(selected_x, selected_y):
            return False

        if board.consist_of(selected_x, selected_y, Apple):
            board.remove_apples(selected_x, selected_y)
            board.create_apples(count=1)
            self.__grow(selected_x=selected_x, selected_y=selected_y)

        else:
            current_head = self.__head
            current_tail = self.__tail

            next_current_tail = current_tail.next_part

            board.remove_content(current_tail.x, current_tail.y, current_tail)

            self.__head = current_tail
            self.__head.x = selected_x
            self.__head.y = selected_y
            self.__head.prev_part = current_head
            self.__head.next_part = None

            current_head.next_part = self.__head

            self.__tail = next_current_tail
            self.__tail.prev_part = None
            board.add_content(self.__head.x, self.__head.y, self.__head)
        
        return True

    def move(self, direction):
        banned_direction = self.NOT_ALLOWED_2_MOVE.get(self.__current_direction)

        if banned_direction != direction:
            handler = self.DIRECTION_2_HANDLERS.get(direction)
            res = handler() if handler else None
            self.__current_direction = direction if res else self.__current_direction 


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

    def get_content(self, content_type):
        for content in self.__contents:
            if isinstance(content, content_type):
                return content
        return None

    def add_contents(self, element):
        return self.__contents.append(element)

    def remove_contents(self, element):
        return self.__contents.remove(element)

    def consist_of(self, content_type):
        for content in self.__contents:
            if isinstance(content, content_type):
                return True

        return False

    def is_empty(self):
        return len(self.__contents) == 0

    def __str__(self):
        return " ".join([str(content) for content in self.__contents])


class Map:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__board = [
            [Cell(x=x, y=y) for x in range(self.__width)]
            for y in range(self.__height)
        ]

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def add_content(self, x, y, element):
        cell = self.__board[y][x]
        cell.add_contents(element)

    def remove_content(self, x, y, element):
        cell = self.__board[y][x]
        cell.remove_contents(element)

    def get_content(self, x, y, content_type):
        return self.__board[y][x].get_content(content_type)

    def consist_of(self, x, y, content_type):
        return self.__board[y][x].consist_of(content_type)

    def is_empty(self, x, y):
        return self.__board[y][x].is_empty()

    def remove_apples(self, x, y):
        apple = board.get_content(x, y, Apple)
        board.remove_content(x, y, apple)

    def create_apples(self, count=4):
        counter = 0

        while counter < count:
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)

            if self.is_empty(x, y):
                apple = Apple(x, y)
                apple.plant()
                counter += 1

    def print_board(self):
        os.system("clear")

        roof = "-" * ((CELL_WIDTH + 1) * self.__width + 1)
        for row in self.__board:
            print(f"{roof}")
            print(Style.CYAN + "|" + "|".join([str(cell).center(CELL_WIDTH)for cell in row]) + "|")

        print(f"{roof}")


class Engine:

    def __init__(self):
        self.__apple_initial_count = 4
        self.__direction = None

    def keyboard_listener(self):
        while True:
            if game_is_over:
                break
            
            action_key = keyboard.read_key()

            if keyboard.is_pressed(action_key):
                self.__direction = action_key

    def snake_automove_listener(self):
        while True:
            if game_is_over:
                break

            time.sleep(0.5)
            self._snake.move(self.__direction)

    def run(self):
        global board, game_is_over

        board = Map(height=10, width=10)
        game_is_over = False
        
        self._snake = Snake(
            h_initial_x=1,
            h_initial_y=1,
            t_initial_x=0,
            t_initial_y=1,
            current_direction="right"
        )
        self.__direction = "right"

        board.create_apples(count=self.__apple_initial_count)

        board_listener = threading.Thread(target=self.keyboard_listener)
        board_listener.start()

        snake_listener = threading.Thread(target=self.snake_automove_listener)
        snake_listener.start()

        while True:
            if game_is_over:
                print(Style.RED + GAME_OVER_TEXT)
                exit(0)
            
            time.sleep(0.1)
            board.print_board()


engine = Engine()
engine.run()
