# tkinter
# pygame
# pyqt5

"""
Cell:
W: wall
P: path
F: finish
"""

# variable

mp = None
is_finished = False

# Constant 

# cell type
WALL = "W"
PATH = "P"
FINISH = "F"

BOMBERMAN = "M"
BOMBERMAN_INIT_X = 0
BOMBERMAN_INIT_Y = 0
BOMB = "B"

# direction
RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

CELL_WIDTH = 11

class Cell:
    
    def __init__(self, x, y, typ=PATH) -> None:
        # private property
        self._x = x
        self._y = y
        self._typ = typ
        self._contents = []

    @property
    def typ(self):
        return self._typ

    @property
    def contents(self):
        return self._contents

    def add_content(self, obj):
        self._contents.append(obj)

    def remove_content(self, obj):
        self._contents.remove(obj)

    def __str__(self):
        rep = ""
        if self._typ == WALL:
           rep = self._typ
        elif self._typ == PATH:
            rep = ", ".join(map(str, self._contents)) 
        else:
            rep = self._typ

        return f"{rep}".center(CELL_WIDTH)


class Map:
    
    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width
        self._board = []

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @property
    def board(self):
        return self._board

    def initial_board(self):
        # height * width
        # height: 4, 0, 1, 2, 3, 4, 5
        # width: 4, 0, ..., 7
        for y in range(self._height):
            rows = []
            for x in range(self._width):
                rows.append(Cell(x=x, y=y))
            
            self._board.append(rows)

    def print_board(self):
        """
        board = [
            [cell, cell, cell, cell], # rows 
            [cell, cell, cell, cell], 
            [cell, cell, cell, cell], 
            [cell, cell, cell, cell]
        ]
        -------------------------------------------------------------------------
        |           |           |           |           |           |           |
        -------------------------------------------------------------------------
        |           |           |           |           |           |           |
        -------------------------------------------------------------------------
        |           |           |           |           |           |           |
        -------------------------------------------------------------------------
        |           |           |           |           |           |           |
        -------------------------------------------------------------------------
        """
        # 6 * 11 + (6 + 1) = ^ * 12 + 1
        ceil_width = (CELL_WIDTH + 1) * self._width + 1
        for rows in self._board:
            # rows: [cell, cell, cell, cell]
            # |           |           |           |           |           |           |
            # 
            print("-" * ceil_width)
            print(f"|{'|'.join(map(str, rows))}|")

        print("-" * ceil_width)


class BomberMan:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        mp.board[y][x].add_content(self)

    def move(self, direction):
        global is_finished

        new_x, new_y = None, None

        if direction == RIGHT:
            new_x = self._x + 1
            new_y = self._y
        elif direction == LEFT:
            new_x = self._x - 1
            new_y = self._y
        elif direction == UP:
            new_x = self._x
            new_y = self._y - 1
        elif direction == DOWN:
            new_x = self._x
            new_y = self._y + 1
        else:
            raise ValueError("Invalid direction, valid directions are: [R, L, U, D]")

        if not (0 <= new_x < mp.width) or not (0 <= new_y < mp.height):
            print("Can not move!")
            return 

        next_cell = mp.board[new_y][new_x]
        if next_cell.typ == WALL:
            print("Can not move!")
            return 
        elif next_cell.typ == FINISH:
            is_finished = True
            return 
        else:
            # remove from prev current
            current_cell = mp.board[self._y][self._x]       
            current_cell.remove_content(self)
            
            self._x = new_x
            self._y = new_y
            next_cell.add_content(self)

    def plant_bomb(self):
        pass    


    def __str__(self):
        return BOMBERMAN

class Bomb:
    pass


class GameEngine:
    def __init__(self):
        pass

    def start(self):
        global mp
        mp = Map(height=4, width=6)
        mp.initial_board()
        bm = BomberMan(x=BOMBERMAN_INIT_X, y=BOMBERMAN_INIT_Y)

        while not is_finished:
            mp.print_board()
            direction = input("Direction: ")
            bm.move(direction=direction)


ge = GameEngine()
ge.start()