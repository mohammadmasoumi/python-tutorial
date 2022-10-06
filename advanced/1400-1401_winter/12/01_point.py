class Point:

    def __init__(self, x, y):
        # constructor
        # _ => private property
        self._x = x
        self._y = y

    def __add__(self, other):

        if isinstance(other, int):
            return Point(self._x + other, self._y + other)

        if isinstance(other, Point):
            return Point(self._x + other._x, self._y + other._y)

    def __str__(self):
        return f"Point at x: {self._x}, y: {self._y}"


point1 = Point(10, 10)
point2 = Point(20, 20)

# str_point1 = str(point1)
# print(str_point1)
print(point1)
print(point1 + point2)
print(point1 + 100)