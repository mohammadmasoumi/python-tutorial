# Dunder method or magic function
# __sth__

"""
        y
        ^
        | 
        |   O
        |
----------------> x
        |
        |
        |


 X  Y
(2, 2)
"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_value):
        # new_value: 10
        # new_value in (int, float)
        if isinstance(new_value, (int, float)):
            self.__x = new_value
        else:
            print("can't assign new value to x.")

    @x.deleter
    def x(self):
        print("can't delete x.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_value):
        # new_value: 10
        # new_value in (int, float)
        if isinstance(new_value, (int, float)):
            self.__y = new_value
        else:
            print("can't assign new value to y.")

    @y.deleter
    def y(self):
        print("can't delete y.")

    def __add__(self, point):
        # p1 + p2
        # self: p1
        # point: p2
        # --------
        # p2 + p1
        # self: p2
        # point: p1

        if isinstance(point, (Point, )):
            return Point(self.__x+point.x, self.__y+point.y)
        else:
            print(f"can't add {type(point)} with Point.")

    def __str__(self):
        return f"({self.__x}, {self.__y})"


p1 = Point(10, 10)
p1.x = 20
p1.y = 20
del p1.x
p2 = Point(5, 5)

# str(p1) -> p1.__str__
# str(p2) -> p2.__str__
print(p1, p2)  # str(p1), str(p2)

# p1 + p2 = p3(p1.x + p2.x, p1.y + p2.y)
# dunder method

# p1.__add__(p2)
print(p1 + p2)
p1 + 10  # Error
p1 + "string"

# int.__add__(p1)
# TypeError: unsupported operand type(s) for +: 'int' and 'Point'
10 + p1

# 10 + p1
# int.__add__(p1)
# p1 + 10
# Point.__add__(10)
