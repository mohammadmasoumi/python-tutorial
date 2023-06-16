from random import randint

"""
|   |   |   |   |   |   |     
| X | X |   |   |   |   |  
|   |   |   |   |   |   |  
|   |   |   |   |   |   |  
|   |   |   |   |   |   |  
|   |   |   |   |   |   |  
| X | X | X |   |   |   |  

Cell
Map
ShipPart
Ship

|   |   |   |   |   |   |     
| X | X |   |   |   |   |  
|   |   |   |   |   |   |  
|   |   |   |   |   |   |  
|   |   |   |   |   |   |  
|   |   |   |   |   |   |  
| X | X | X |   |   |   |  

Cell
Map
Bomb

---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
---------------------------------------------------------------------------------

"""
# constant properties
CELL_WIDTH = 7

# Pascal casing


class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.reveal = False
        self.__contents = [0]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def has_content(self, element):
        return element in self.__contents

    def has_typ(self, typ):
        for element in self.__contents:
            if isinstance(element, typ):
                return True

        return False

    def get_content(self):
        return self.__contents

    def add_content(self, element):
        self.__contents.append(element)

    def clear_content(self):
        self.__contents.clear()

    def remove_content(self, element):
        self.__contents.remove(element)

    def __str__(self):  # string representation of instance of Cell
        # self.__contents: [Bomb, Number]
        # "".join([]) -> list of string
        # self.__contents = [20, 30]
        # map(str, self.__contents)
        # ["20", "30"]
        # "-".join(["20", "30"])
        # "20-30"
        if self.reveal:
            return "-".join(map(str, self.__contents))
        else:
            return ""

# cell = Cell(10, 10)
# cell.add_content(20)
# cell.add_content(30)
# cell.add_content(40)
# print(cell)  # print(str(cell))
# cell.remove_content(20)
# print(cell)
# print(cell.has_content(30))
# print(cell.has_content(20))
# # AttributeError: 'Cell' object has no attribute '__x'
# print(cell.x, cell.y)


class Map:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.__board = [
            [Cell(x=x, y=y) for x in range(self.__width)]
            for y in range(self.__height)
        ]

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # def add_content(self, x, y, element):
    #     """
    #     self.__board = [
    #         [Cell, Cell, Cell, Cell], # 0
    #         [Cell, Cell, Cell, Cell], # 1
    #         [Cell, Cell, Cell, CCell], # 2
    #         [Cell, Cell, Cell, Cell] # 3
    #     ]
    #                        y
    #     row = self.__board[2]
    #     cell = row[3] # CCell
    #                         y  x
    #     cell = self.__board[2][3]

    #     """
    #     # Cell: self.__board[y][x]
    #     # Cell.add_content(element)
    #     cell = self.__board[y][x]
    #     cell.add_content(element=element)

    def get_cell(self, x, y):
        return self.__board[y][x]

    # def get_content(self, x, y):
    #     return self.__board[y][x]

    # def has_typ(self, x, y, typ):
    #     cell = self.__board[y][x]
    #     return cell.has_typ(typ)

    # def remove_content(self, x, y, element):
    #     cell = self.__board[y][x]
    #     cell.remove_content(element=element)

    # def reveal_content(self, x, y):
    #     cell = self.__board[y][x]
    #     cell.reveal = True

    def __str__(self):
        board_str = ""
        """
        print("|      |      |     |\n|      |      |     |\n|      |      |     |\n")

        ----------------------
        |      |      |      |
        ----------------------
        |      |      |      |
        ----------------------
        |      |      |      |
        ----------------------

        (((CELL_WIDTH + 1) * self.__width) + 1) * "-"

        """
        ceil = ((((CELL_WIDTH + 1) * self.__width) + 1) * "-") + "\n"
        for row in self.__board:
            #  [Cell, Cell, Cell, Cell]
            #  ["", "", "", "20-30"]
            # map(str, row)
            # str(cell) -> __str__
            # cast to string
            # "m".center(11)
            # -----m-----
            # "20-30".center(11)
            # ---20-30---
            # hello | bye | goodbyte
            # | hello | bye | goodbyte |
            board_str += ceil
            board_str += "|" + \
                "|".join(map(lambda c: str(c).center(CELL_WIDTH), row)) + "|\n"

        board_str += ceil
        return board_str


#                dx  dy
RELATIVE_POS = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                (1, 0), (-1, 1), (0, 1), (1, 1)]


class Bomb:

    def __init__(self, x, y):
        # self: current object

        self.__x = x
        self.__y = y

        # global board

        # cell = board.get_cell(x, y)
        # cell.clear_content()
        # cell.add_content(self)

        # """
        # -------------------------
        # |x-1,y-1|x,y-1  |x+1,y-1|
        # -------------------------
        # |x-1,y  | x,y   |x+1,y  |
        # -------------------------
        # |x-1,y+1|x,y+1  |x+1,y+1|
        # -------------------------
        # """
        # # dx, dy = (-1, -1)
        # for dx, dy in RELATIVE_POS:
        #     cx = self.__x + dx
        #     cy = self.__y + dy

        #     if (0 <= cx < board.width) and (0 <= cy < board.height):
        #         cell = board.get_cell(cx, cy)
        #         if not cell.has_typ(Bomb):
        #             contents = cell.get_content()  # []
        #             contents[0] += 1

    def add_board(self):
        global board

        cell = board.get_cell(self.__x, self.__y)
        cell.clear_content()
        cell.add_content(self)

        """
        -------------------------
        |x-1,y-1|x,y-1  |x+1,y-1|
        -------------------------
        |x-1,y  | x,y   |x+1,y  |
        -------------------------
        |x-1,y+1|x,y+1  |x+1,y+1|
        -------------------------
        """
        # dx, dy = (-1, -1)
        for dx, dy in RELATIVE_POS:
            cx = self.__x + dx
            cy = self.__y + dy

            if (0 <= cx < board.width) and (0 <= cy < board.height):
                cell = board.get_cell(cx, cy)
                if not cell.has_typ(Bomb):
                    contents = cell.get_content()  # []
                    contents[0] += 1

    def __str__(self):
        return "B"  # 💣


board = None


class Engine:

    def __init__(self, bomb_count, map_width, map_height):
        self.__bomb_count = bomb_count
        self.__map_width = map_width
        self.__map_height = map_height

    def run(self):
        global board
        board = Map(width=self.__map_width, height=self.__map_height)

        bomb_cnt = 0
        while bomb_cnt < self.__bomb_count:
            # Return random integer in range [a, b], including both end points.
            cx = randint(0, self.__map_width-1)
            cy = randint(0, self.__map_height-1)

            c_cell = board.get_cell(cx, cy)
            if not c_cell.has_typ(Bomb):
                bomb = Bomb(x=cx, y=cy)
                bomb.add_board()
                bomb_cnt += 1

                # bomb1 = Bomb(x=0, y=0)
                # bomb2 = Bomb(x=1, y=0)

        is_gameover = False
        revealed_non_bomb_cell = 0
        total_non_bomb_cell = (self.__map_height *
                               self.__map_height) - self.__bomb_count
        print(board)
        while not is_gameover:

            if revealed_non_bomb_cell == total_non_bomb_cell:
                is_gameover = True
                print("🎈You won!")

            x, y = list(map(int, input("x, y: ").split()))

            if (0 <= x < self.__map_width) and (0 <= y < self.__map_height):
                cell = board.get_cell(x, y)
                cell.reveal = True

                if cell.has_typ(Bomb):
                    is_gameover = True
                    print("Hahaha 🎃, you lost!")
                else:
                    revealed_non_bomb_cell += 1

            print(board)


# board.reveal_content(x=0, y=0)
# board.reveal_content(x=1, y=1)
# print(board)


engine = Engine(10, 5, 5)
engine.run()
