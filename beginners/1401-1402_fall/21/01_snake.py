import os
import time
import keyboard
import random

CELL_WIDTH = 11


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
        return "*"


class Snake:

    def __init__(self, h_initial_x, h_initial_y, t_initial_x, t_initial_y, current_direction):
        head = SnakePart(h_initial_x, h_initial_y)
        tail = SnakePart(t_initial_x, t_initial_y, next_part=head)

        head.prev_part = tail

        board.add_content(head.x, head.y, head)
        board.add_content(tail.x, tail.y, tail)

        self.__head = head
        self.__tail = tail

        self.__current_direction = current_direction

    def __is_game_over(self, selected_x, selected_y):
        hit_itself = board.is_consist_of(
            x=selected_x,
            y=selected_y,
            content_type=SnakePart
        )

        out_of_range = not ((0 <= selected_x < board.width)
                            or (0 <= selected_y < board.height))

        return hit_itself or out_of_range

    def __move(self, new_head_x, new_head_y):

        if self.__is_game_over(selected_x=new_head_x, selected_y=new_head_y):
            is_gameover = True
            return

        old_tail = self.__tail
        old_head = self.__head

        old_tail_next_part = old_tail.next_part

        board.remove_content(old_tail.x, old_tail.y, old_tail)

        self.__head = old_tail
        self.__head.x = new_head_x
        self.__head.y = new_head_y
        self.__head.prev_part = old_head
        self.__head.next_part = None

        old_head.next_part = self.__head

        self.__tail = old_tail_next_part
        self.__tail.prev_part = None

        board.add_content(self.__head.x, self.__head.y, self.__head)

    def __move_up(self):
        if self.__current_direction != "down":
            next_x, next_y = self.__head.x, self.__head.y - 1
            self.__move(next_x, next_y)
            self.__current_direction = "up"

    def __move_down(self):
        if self.__current_direction != "up":
            next_x, next_y = self.__head.x, self.__head.y + 1
            self.__move(next_x, next_y)
            self.__current_direction = "down"

    def __move_right(self):
        if self.__current_direction != "left":
            next_x, next_y = self.__head.x + 1, self.__head.y
            self.__move(next_x, next_y)
            self.__current_direction = "right"

    def __move_left(self):
        if self.__current_direction != "right":
            next_x, next_y = self.__head.x - 1, self.__head.y
            self.__move(next_x, next_y)
            self.__current_direction = "left"

    def move(self, direction):
        DIRECTION_2_HANDLERS = {
            "right": self.__move_right,
            "left": self.__move_left,
            "up": self.__move_up,
            "down": self.__move_down,
        }
        handler = DIRECTION_2_HANDLERS.get(direction)
        handler() if handler else None


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

    def add_contents(self, element):
        return self.__contents.append(element)

    def remove_contents(self, element):
        return self.__contents.remove(element)

    def is_consist_of(self, content_type):
        for content in self.__contents:
            if isinstance(content, content_type):
                return True

        return False

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

    def is_consist_of(self, x, y, content_type):
        self.__board[y][x].is_consist_of(content_type)

    def print_board(self):
        roof = "-" * ((CELL_WIDTH + 1) * self.__width + 1)

        for row in self.__board:
            print(f"{roof}")
            print("|" + "|".join([str(cell).center(CELL_WIDTH)
                  for cell in row]) + "|")

        print(f"{roof}")


class Apple:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def plant(self):
        board.add_content(self.__x, self.__y, self)

    def __str__(self):
        return "A"  # "🍎"


class Engine:

    def __init__(self):
        self.__apple_num = 4

    def plant_random_apple(self):
        counter = 0

        while counter < self.__apple_num:
            x = random.randint(0, board.width - 1)
            y = random.randint(0, board.height - 1)

            apple = Apple(x, y)
            apple.plant()

            counter += 1

    def run(self):
        global board, is_gameover
        is_gameover = False
        board = Map(height=10, width=10)
        self.plant_random_apple()

        snake = Snake(
            h_initial_x=1,
            h_initial_y=1,
            t_initial_x=0,
            t_initial_y=1,
            current_direction="right"
        )

        while True:
            board.print_board()
            time.sleep(1)
            snake.move("right")
            # os.system('cls')

            # direction = keyboard.read_key()

            # if direction == "up":
            #     if keyboard.is_pressed("up"):
            #         pass
            # elif direction == "down":
            #     if keyboard.is_pressed("down"):
            #         pass


engine = Engine()
engine.run()
