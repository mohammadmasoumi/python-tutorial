
"""
-----------------------------------------
| R  |    |    |    |    |    |    |    |
-----------------------------------------   
|    |    |    |    |  # |    |    |    |
-----------------------------------------   
|    | R  |    |%%%%|    |    |    |    |
-----------------------------------------   
|    |    |    |%%%%|  # |    |    |    |
-----------------------------------------   
|    |    |    |%%%%|    |    |    |    |
-----------------------------------------   
|    |    |    | #  |    |    |    |    |
-----------------------------------------   
|    |    |    |%%%%|    |    |    |    |
-----------------------------------------   
|    |    |    |    |    |    |    |    |
-----------------------------------------   

a -> left
s -> down
w -> up
d -> right

wall 
random movement
"""
from random import randint, choice

# board properties
WIDTH = 10
HEIGHT = 10

# cell properties
CELL_WIDHT = 11
N_WALL = 10
N_RANDOM_DIRECTION = 5

# robot properties
robot_x = 0
robot_y = 0

# cell properties
ROBOT_SIGN = "R"
WALL_SIGN = "%"
RANDOM_DIRECTION_SIGN = "#"

DIRECTIONS = "aswd"

board = None
# controller = None

def initialize_board():
    global board

    board = [["" for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # initialize robot
    board[robot_y][robot_x] = ROBOT_SIGN 

    # initialize wall
    n_wall = 0
    while n_wall < N_WALL:
        x_pos = randint(0, WIDTH - 1)
        y_pos = randint(0, HEIGHT - 1)

        if not ((x_pos == robot_x and y_pos == robot_y) or board[y_pos][x_pos] == WALL_SIGN):
            board[y_pos][x_pos] = WALL_SIGN * CELL_WIDHT
            n_wall += 1
            
    # initialize random direction 
    n_random_direction = 0
    while n_random_direction < N_RANDOM_DIRECTION:
        x_pos = randint(0, WIDTH - 1)
        y_pos = randint(0, HEIGHT - 1)

        if not ((x_pos == robot_x and y_pos == robot_y) or board[y_pos][x_pos] == WALL_SIGN or board[y_pos][x_pos] == RANDOM_DIRECTION_SIGN):
            board[y_pos][x_pos] = RANDOM_DIRECTION_SIGN
            n_random_direction += 1

def print_board():
    ceil_length = (CELL_WIDHT + 1) * WIDTH + 1
    print("-" * ceil_length)

    for row in board:
        # row: list
        print("|" + "|".join(map(lambda x: str(x).center(11), row)) + "|")
        print("-" * ceil_length)

def move_right():
    global robot_x
    new_x = robot_x + 1

    if 0 <= new_x < WIDTH:
        if board[robot_y][new_x] == WALL_SIGN * CELL_WIDHT:
            print("Can't move right! There is a wall.")
        elif board[robot_y][new_x] == RANDOM_DIRECTION_SIGN:
            board[robot_y][robot_x] = ""
            robot_x = new_x
            controller.get(choice(DIRECTIONS))()
        else:
            if board[robot_y][robot_x] != RANDOM_DIRECTION_SIGN:
                board[robot_y][robot_x] = ""
            robot_x = new_x
            board[robot_y][robot_x] = ROBOT_SIGN

def move_left():
    global robot_x
    new_x = robot_x - 1

    if 0 <= new_x < WIDTH:
        if board[robot_y][new_x] == WALL_SIGN * CELL_WIDHT:
            print("Can't move left! There is a wall.")
        elif board[robot_y][new_x] == RANDOM_DIRECTION_SIGN:
            board[robot_y][robot_x] = ""
            robot_x = new_x
            controller.get(choice(DIRECTIONS))()
        else:
            if board[robot_y][robot_x] != RANDOM_DIRECTION_SIGN:
                board[robot_y][robot_x] = ""
            robot_x = new_x
            board[robot_y][robot_x] = ROBOT_SIGN

def move_up():
    global robot_y
    new_y = robot_y - 1

    if 0 <= new_y < HEIGHT:
        if board[new_y][robot_x] == WALL_SIGN * CELL_WIDHT:
            print("Can't move up! There is a wall.")
        elif board[new_y][robot_x] == RANDOM_DIRECTION_SIGN:
            board[robot_y][robot_x] = ""
            robot_y = new_y
            controller.get(choice(DIRECTIONS))()
        else:
            if board[robot_y][robot_x] != RANDOM_DIRECTION_SIGN:
                board[robot_y][robot_x] = ""
            robot_y = new_y
            board[robot_y][robot_x] = ROBOT_SIGN

def move_down():
    global robot_y
    new_y = robot_y + 1

    if 0 <= new_y < HEIGHT:
        if board[new_y][robot_x] == WALL_SIGN * CELL_WIDHT:
            print("Can't move down! There is a wall.")
        elif board[new_y][robot_x] == RANDOM_DIRECTION_SIGN:
            board[robot_y][robot_x] = ""
            robot_y = new_y
            controller.get(choice(DIRECTIONS))()
        else:
            if board[robot_y][robot_x] != RANDOM_DIRECTION_SIGN:
                board[robot_y][robot_x] = ""
            robot_y = new_y
            board[robot_y][robot_x] = ROBOT_SIGN

initialize_board()

controller = {
    "a": move_left,
    "s": move_down,
    "w": move_up,
    "d": move_right
}
# def invalid_input():
#     print("Invalid input")

while True:
    print_board()
    # controller.get(input()): function
    # controller: dict
    # controller.get(input()): function
    # controller.get(input())(): function()
    # controller.get(input(), invalid_input)()
    controller.get(input(), lambda : print("Invalid input"))()

    # None() raise exception
    # direction_method = controller.get(input(), None)
    # if direction_method:
    #     direction_method()
