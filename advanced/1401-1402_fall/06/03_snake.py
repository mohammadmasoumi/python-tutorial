import time
import keyboard


CELL_WIDTH = 11
board = None


class Direction:

    UP = "up"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Cell:

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

        self.__contents = []

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def add_content(self, element):
        self.__contents.append(element)

    def remove_content(self, element):
        self.__contents.remove(element)

    def has_content(self, element):
        return element in self.__contents

    def __str__(self) -> str:
        return ",".join([str(content) for content in self.__contents])


class Board:

    def __init__(self, height, width) -> None:
        self.__height = height
        self.__width = width
        self.__map = [[Cell(x=x, y=y) for x in range(width)]
                      for y in range(height)]

    def __get_cell(self, x, y):
        return self.__map[y][x]

    def add_content(self, x, y, element):
        cell = self.__get_cell(x, y)
        cell.add_content(element)

    def remove_content(self, x, y, element):
        cell = self.__get_cell(x, y)
        cell.remove_content(element)

    def print_map(self):
        roof = "-" * (((CELL_WIDTH + 1) * self.__width) + 1)

        for y in range(self.__height):
            cells = self.__map[y]
            # roof = "-" * ((CELL_WIDTH * self.__width) + (self.__width + 1))
            row = "|" + "|".join([str(cell).center(CELL_WIDTH)
                                 for cell in cells]) + "|"

            print(roof)
            print(row)

        print(roof)


class SnakePart:

    def __init__(self, x, y, has_taken) -> None:
        self.__x = x
        self.__y = y
        self.__has_taken = has_taken

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def has_taken(self):
        return self.__has_taken

    @has_taken.setter
    def has_taken(self, value):
        self.__has_taken = value


class Snake:

    def __init__(self, name, initial_x, initial_y) -> None:
        self.name = name
        head = SnakePart(x=initial_x, y=initial_y, has_taken=True)

        self.__head = head
        self.__parts = [head]

        board.add_content(initial_x, initial_y, self)

    def __move_right_handler(self):
        next_x, next_y = self.__head.x + 1, self.__head.y

        for part in self.__parts:
            prev_x = part.x
            prev_y = part.y

            board.remove_content(prev_x, prev_y, self)

            part.x = next_x
            part.y = next_y

            board.add_content(next_x, next_y, self)

            next_x = prev_x
            next_y = prev_y


    def __move_left_handler(self):
        next_x, next_y = self.__head.x - 1, self.__head.y

        for part in self.__parts:
            prev_x = part.x
            prev_y = part.y

            board.remove_content(prev_x, prev_y, self)

            part.x = next_x
            part.y = next_y

            board.add_content(next_x, next_y, self)

            next_x = prev_x
            next_y = prev_y

    def __move_down_handler(self):
        next_x, next_y = self.__head.x, self.__head.y + 1

        for part in self.__parts:
            prev_x = part.x
            prev_y = part.y

            board.remove_content(prev_x, prev_y, self)

            part.x = next_x
            part.y = next_y

            board.add_content(next_x, next_y, self)

            next_x = prev_x
            next_y = prev_y

    def __move_up_handler(self):
        next_x, next_y = self.__head.x, self.__head.y - 1

        for part in self.__parts:
            prev_x = part.x
            prev_y = part.y

            board.remove_content(prev_x, prev_y, self)

            part.x = next_x
            part.y = next_y

            board.add_content(next_x, next_y, self)

            next_x = prev_x
            next_y = prev_y

    def move(self, direction):

        DIRECTION_2_HANDLERS = {
            Direction.DOWN: self.__move_down_handler,
            Direction.UP: self.__move_up_handler,
            Direction.RIGHT: self.__move_right_handler,
            Direction.LEFT: self.__move_left_handler,
        }

        handler = DIRECTION_2_HANDLERS.get(direction)
        handler() if handler else None



    def __str__(self):
        return "😎"


class Engine:

    KEYS = (
        "up",
        "down",
        "left",
        "right",
        "esc",
        "space",
        "s",
    )

    def __init__(self, rnd, map_height, map_width, snake_initial_x, snake_initial_y) -> None:
        self.__rnd = rnd
        self.__curr_direction = Direction.DOWN
        self.__is_paused = False

        global board
        board = Board(height=map_height, width=map_width)

        self.__snake = Snake(
            name="Dragon",
            initial_x=snake_initial_x,
            initial_y=snake_initial_y
        )

    def __on_move_up(self):
        self.__curr_direction = Direction.UP

    def __on_move_down(self):
        print("Moving down ...")
        self.__curr_direction = Direction.DOWN

    def __on_move_left(self):
        self.__curr_direction = Direction.LEFT

    def __on_move_right(self):
        self.__curr_direction = Direction.RIGHT

    def __on_save(self):
        pass

    def __on_pause(self):
        self.__is_paused = not self.__is_paused

    def __on_exit(self):
        exit(0)

    def run(self):
        KEY_2_HANDLER = {
            "up": self.__on_move_up,
            "down": self.__on_move_down,
            "left": self.__on_move_left,
            "right": self.__on_move_right,
            "esc": self.__on_exit,
            "space": self.__on_pause,
            "s": self.__on_save,
        }

        while True:
            self.__rnd += 1
            time.sleep(1)
            board.print_map()

            action_key = keyboard.read_key(suppress=True)
            # keyboard.on_press_key("down", self.__on)
            print(f"action_key: {action_key}")

            # for key in self.KEYS:
            # if keyboard.is_pressed(action_key):
            handler = KEY_2_HANDLER.get(action_key)
            handler() if handler else None

            if not self.__is_paused:
                self.__snake.move(self.__curr_direction)


engine = Engine(20, 10, 10, 0, 0)
engine.run()
