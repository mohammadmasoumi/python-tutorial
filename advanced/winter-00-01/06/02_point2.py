class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

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


point1 = Point(10, 10)
point2 = Point(20, 20)

print(point1 + 12)
print(point1 + point2)
print(point1 * 12)
print(point1 * point2)