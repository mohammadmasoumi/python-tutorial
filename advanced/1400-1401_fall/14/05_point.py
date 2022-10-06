class Point:

    def __init__(self, x, y):
        # def __init__(self):
        # self._x = None
        self._x = x
        # self._y = None
        self._y = y

    # def set_x(self, x):
    #     self._x = x
    #
    # def set_y(self, y):
    #     self._y = y
    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self._x * other, self._y * other)
        # return None

    def __floordiv__(self, other):
        if isinstance(other, int):
            return Point(self._x // other, self._y // other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Point(self._x / other, self._y / other)

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y)

    def __str__(self):
        return f"({self._x}, {self._y})"

    # int(Point)
    # def __int__(self):
    #

    def __gt__(self, other):
        return self._x > other._x and self._y > other._y

    def __lt__(self, other):
        return self._x < other._x and self._y < other._y


point1 = Point(10, 10)
point2 = Point(20, 20)

# point1.set_x(12)
# point1.set_y(12)

print(point1 + point2)
print(point1 * 2)
print(point1 / 2)
print(point2 > point1)
# point1.+(point2)
