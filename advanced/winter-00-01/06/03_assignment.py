from typing_extensions import runtime


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other , Point ):
            return self.x == other.x and self.y == other.y
        return True

    def __floordiv__(self, other):
        if isinstance(other, int):
            return Point(self.x // other, self.y // other)
        return Point(self.x // other.x, self.y // other.y)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Point(self.x / other, self.y / other)
        return Point(self.x / other.x, self.y / other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        return Point(self.x * other.x, self.y * other.y)

    def __add__(self, other):
        if isinstance(other, int):
            return Point(self.x + other, self.y + other)

        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __int__(self) -> int:
        return self.x + self.y

    def __float__(self):
        return float(self.x + self.y)


point1 = Point(24, 24)
point2 = Point(2, 2)
print(point1+12)
print(point1+point2)
print("---------------------------------------------------")
print(point1*12)
print(point1*point2)
print("---------------------------------------------------")
print(point1/12)
print(point1/point2)
print("---------------------------------------------------")
print(point1//12)
print(point1//point2)
print("---------------------------------------------------")
print(int(point1))
print(float(point1))
print(point1[0])
print(point1[1])
print("---------------------------------------------------")


