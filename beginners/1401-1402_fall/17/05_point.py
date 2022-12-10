
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        # point1 + 10
        # point1 + point2
        # point1 + "hello"
        if isinstance(obj, Point):
            return Point(self.x + obj.x, self.y + obj.y)
        elif isinstance(obj, (int, str, float, bool)):
            raise ValueError(f"Unsupported {type(self)} + {type(obj)}")

    def __str__(self):
        return f"({self.x}, {self.y})"


point1 = Point(10, 10)
point2 = Point(8, 5)
print(point1)
print(point2)
#      self  + obj
# point1.__add__(12)
# print(point1 + 12)
# 12.__add__(point1)
# print(12 + point1)

print(point1 + "hello")
print(point1 + point2)
