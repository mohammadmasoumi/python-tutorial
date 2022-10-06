
from board import board, board_width, board_length, print_board
from random import randint

# variable
bomb_count = 5
around_bomb_square = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)    
]

#             a         b
# create a random int from a, b
# print(randint(0, board_width - 1))
def plant_bombs():
    def cover_bomb_squre_with_one(bomb_x, bomb_y):
        for item in around_bomb_square:
            # item: (1, 1)
            # diff_x: item[0]
            # diff_y = item[1]
            # unpacking
            diff_x, diff_y = item
            cell_x = bomb_x + diff_x
            cell_y = bomb_y + diff_y

            if 0 <= cell_x < board_width and 0 <= cell_y < board_length and board[cell_y][cell_x] != 2:
                board[cell_y][cell_x] = 1
            
    for _ in range(bomb_count):
        bomb_x = randint(0, board_width - 1)
        bomb_y = randint(0, board_length - 1)
        board[bomb_y][bomb_x] = 2
        cover_bomb_squre_with_one(bomb_x, bomb_y)
        # print(bomb_x, bomb_y)

plant_bombs()
print_board()


