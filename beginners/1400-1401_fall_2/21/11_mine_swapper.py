from random import randint

board_width = 10
board_length = 10 
board = []

for y in range(board_length):
    new_row = []
    for x in range(board_width):
       new_row.append(dict(value=0, is_show=False))
    board.append(new_row)

cell_length = 3
ceil_length = (cell_length + 1) * board_width + 1 
bomb_count = 5
cells_around_bomb = [(-1, -1), (0, -1), (+1, -1), (-1, 0), (+1, 0), (-1, +1), (0, +1), (+1,+1)]

""" 4x4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

----------X----------
|    0    1    2
| 0  [x-1, y-1][x  , y-1][x+1, y-1]
Y 1  [x-1, y  ][x  , y  ][x+1, y  ]
| 2  [x-1, y+1][x  , y+1][x+1, y+1]
|
[(-1, -1), (0, -1), (+1, -1), (-1, 0), (+1, 0), (-1, +1), (0, +1), (+1,+1)]

[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------
"""

def print_board():
    def str_center(item):
        # item = [{"value": 0, "is_show": False}
        # item.center(3, "-")
        # " 0 "
        cell = str(item.get("value")) if item.get("is_show") else "X"
        return cell.center(cell_length)
    
    ceil = "-" * ceil_length
    print(ceil)

    for row in board:
        # row = [{"value": 0, "is_show": False}, {"value": 0, "is_show": False}, {"value": 0, "is_show": False}, {"value": 0, "is_show": False}]
        # rwo = [0, 0, 0, 0]
        # [' 0 ', ' 0 ', ' 0 ', ' 0 ', ' 0 ', ' 0 ', ' 0 ', ' 0 ', ' 0 ', ' 0 ']
        # print(list(map(str_center, row)))
        #  0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
        # print("|".join(map(str_center, row)))
        row_cell = "|" + "|".join(map(str_center, row)) + "|"
        print(row_cell)
        print(ceil)


def select_bombs():
    global board

    # cells_around_bomb = [(-1, -1), (0, -1), (+1, -1), (-1, 0), (+1, 0), (-1, +1), (0, +1), (+1,+1)]
    def update_bomb_boarder(x, y):
        for diff_x, diff_y in cells_around_bomb:
            # (-1, -1)
            # diff_x = -1
            # diff_y = -1
            new_x = x + diff_x
            new_y = y + diff_y

            # 0 <= new_x < 10
            if (0 <= new_x < board_width) and (0 <= new_y < board_length) and board[new_y][new_x] != 2:
                board[new_y][new_x].update(value=1)

    for _ in range(bomb_count):
        x = randint(0, board_width - 1)
        y = randint(0, board_length - 1)

        board[y][x].update(value=2)
        update_bomb_boarder(x, y)


select_bombs()

# 12 12
rounds = 0
while True:
    print_board()
    rounds += 1

    if rounds == (board_width * board_length) - bomb_count:
        print("You win")
        break

    x, y = list(map(int, input().split()))

    if (0 <= x < board_width) and (0 <= y < board_length):
        if board[y][x].get("value") == 2:
            print("Game over")
            break
        else:
            board[y][x].update(is_show=True)
    else:
        print("Invalid input")