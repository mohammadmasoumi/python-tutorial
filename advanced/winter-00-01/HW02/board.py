
# parametrize
board_width = 10
board_length = 10
cell_width = 3

#                  10  *   "| 0 "   +  "|"     
floor_width = board_width * (cell_width + 1) + 1
# 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
# board_width - 1 + 2 =? board_width + 1 
# | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
# (board_width * cell_width) + ( board_width * 1 ) + 1 
# board_width * (cell_width + 1) + 1
# 10 * 3 + 10 + 1 => 41
# 10 * 3 + 10 * 1 + 1
# 10 * (3 + 1) + 1

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board = [0] * 10
# print(board)

"""
# board
[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------

print_board
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
"""
# list comprehenstion
# print(   [   item * 2 for item in [1, 2, 3] if item == 2   ]   )

# variable
# {'is_show': True, 'value': 0}
# board = [[0] * board_width for _ in range(board_length)]
board = []

for _ in range(board_length):
    row = []
    for _ in range(board_width):
        row.append(0)
    board.append(row)

def print_board():
    def cell_repr(item):
        # item: 0, int
        return str(item).center(cell_width)

    floor_repr = "-" * floor_width
    print(floor_repr)
    for row in board:
        # row 
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # map(str, row)
        # ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        # "|".join(map(str, row))
        # 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  
        # join
        # [" 0 ", " 0 ", " 0 ", "0", " 0 ", " 0 ", " 0 ", " 0 ", " 0 ", " 0 "]
        # "|".join(map(cell_repr, row))
        #  0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
        # | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        # ali -> *ali*
        row_repr = "|" + "|".join(map(cell_repr, row)) + "|"
        print(row_repr)
        print(floor_repr)


# print_board()
# print(len("| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |"))

