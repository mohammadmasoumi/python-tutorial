class Cell:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._contents = []

    def add_content(self, obj):
        self._contents.append(obj)

    def remove_content(self, obj):
        self._contents.remove(obj)

    def __str__(self):
        return " | ".join([str(content) for content in self._contents])


class Map:

    def __init__(self, width, length):
        self._width = width
        self._length = length
        self._matrix = None

    def initialize(self):
        self._matrix = []
        for x in range(self._width):
            row = []
            for y in range(self._length):
                cell = Cell(x, y)
                cell.add_content("#")
                row.append(cell)

            self._matrix.append(row)

    def show_map(self):
        # print(self._matrix)
        for x in range(self._length):
            for y in range(self._width):
                print(self._matrix[y][x], end="")
            print("")


my_map = Map(10, 3)
my_map.initialize()
my_map.show_map()
