

# variables
is_finished = False

# board options
row_size = 10
col_size = 10

cell_width = 5
cell_sign = "-"

# robot options
robot_x = 0
robot_y = 0
robot_sign = "X"

# initial board
board = [[cell_sign] * row_size for _ in range(col_size)]
board[robot_y][robot_x] = robot_sign


def print_board():
    """
    print board function
    """
    ceil = cell_sign * ((cell_width + 1) * len(row_size) + 1)
    for row in board:
        print(ceil)
        print("|" + "|".join([col.center(cell_width) for col in row]) + "|")

    print(ceil)


def can_move(new_x, new_y):
    """
    decide whether the robot can move or not

    @param new_x: new robot x
    @param new_y: new robot y
    """
    valid_move = True

    if not (0 <= new_x < row_size):
        print("Can't move!")
        valid_move = False
    elif not (0 <= new_y < row_size):
        print("Can't move!")
        valid_move = False
    else:
        valid_move = True

    return valid_move


def move_right():
    new_x = robot_x + 1
    new_y = robot_y

    if can_move(new_x, new_y):
        # clear prev cell
        board[robot_y][robot_x] = cell_sign

        # update robot coordination
        robot_x, robot_y = new_x, new_y

        # add robot into new cell
        board[robot_y][robot_x] = cell_sign


def move_left():
    pass


def move_up():
    pass


def move_down():
    pass


# direction - movement function mapping
controller = {
    "U": move_up,
    "D": move_down,
    "R": move_right,
    "L": move_left
}

# game engine
while not is_finished:
    direction = input()

    if direction == "EXIT":
        is_finished = True
        continue

    # movement function
    move_function = controller.get(direction)

    # handle invalid keyword
    if not move_function:
        print("Invalid direction")
        continue
