"""
width: 10
height: 10

------------------------------------
|    |    |    |    |    |    |    |
------------------------------------   
| 2  | 2  | 2  |    |    |    |    |
------------------------------------   
| 2  | 3  | 2  |    |    |    |    |
------------------------------------   
| 2  | 2  | 2  |    |    |    |    |
------------------------------------   
|    | 2  | 2  | 2  |    |    |    |
------------------------------------   
|    | 2  | 3  | 2  |    |    |    |
------------------------------------   
|    | 2  | 3  | 2  |    |    |    |
------------------------------------   
|    | 2  | 2  | 2  |    |    |    |
------------------------------------   
|    |    |    |    |    |    |    |
------------------------------------   

1. board preparation
    1.1 set mines
    1.2 set hints(1,2)
    1.3 DO NOT SHOW all numbers at first.
2. board print
3. user interaction
    - 2 5 fee
    - 2 5 bomb
4. finalize game & select winner


[[1, 2] for item in range(10)]

[
    [1, 2], 
    [1, 2],
    [1, 2],
    [1, 2],
    [1, 2],
    [1, 2],
    [1, 2],
    [1, 2],
    [1, 2],
]

[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
-------------------------------------------  
|  1  |  1  |  1  |  1  |  1  |  1  |  1  |
-------------------------------------------

WIDTH = 10
HEIGHT = 10
CELL_WIDHT = 11

my_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("|".join(map(str, my_list)))
print("-" * ((CELL_WIDHT + 1) * WIDTH + 1))
print("|" + "|".join(map(lambda x: str(x).center(11), my_list)) + "|")
print("-" * ((CELL_WIDHT + 1) * WIDTH + 1))
"""
from random import randint

# board properties
WIDTH = 10
HEIGHT = 10
N_BOMBS = 6

# cell properties
CELL_WIDHT = 11
FREE_CELL_VALUE = 1
BOMB_NEIGHBOUR_CELL_VALUE = 2
BOMB_CELL_VALUE = 3

# command properties
FREE_COMMAND = "free"
BOMB_COMMAND = "bomb"

board = [[dict(value=1, has_selected=False) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_board():
    ceil_length = (CELL_WIDHT + 1) * WIDTH + 1
    print("-" * ceil_length)

    for row in board:
        # row: list
        print("|" + "|".join(map(lambda x: str(x.get("value") if x.get('has_selected') else "").center(11), row)) + "|")
        print("-" * ceil_length)


bomb_cell_range = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
def plant_bombs():
    global board

    for _ in range(N_BOMBS):
        x = randint(0, WIDTH - 1)
        y = randint(0, HEIGHT - 1)

        board[y][x].update(value=BOMB_CELL_VALUE)

        for x_diff, y_diff in bomb_cell_range:
            new_x = x + x_diff
            new_y = y + y_diff

            if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
                cell = board[new_y][new_x]
                if cell.get("value") != BOMB_CELL_VALUE:
                    cell.update(value=BOMB_NEIGHBOUR_CELL_VALUE)

plant_bombs()
defused_bombs = 0

while True:
    # 2 5 free
    # 2 4 bomb
    if defused_bombs == N_BOMBS:
        print("You won!")
        break
    
    print_board()
    selected_x, selected_y, command = input().split()

    # board[selected_y][selected_x]: dict
    cell = board[int(selected_y)][int(selected_x)]

    if command == FREE_COMMAND:
        if cell.get("value") == BOMB_CELL_VALUE:
            print("Game over!")
            break
        else:
            cell.update(has_selected=True)
    elif command == BOMB_COMMAND:
        if cell.get("value") == BOMB_CELL_VALUE:
            cell.update(has_selected=True)
            defused_bombs += 1
        else:
            print("Game over!")
            break
    else:
        print("Invalid command!")
