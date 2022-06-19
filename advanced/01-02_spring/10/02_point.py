# 
# "Ali" + "Asghar" 
# magic function, dunder function

class Point:
    _counts = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        Point._counts += 1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # operation
    def __add__(self, obj):
        # type obj ???
        # point1 + point2
        # self: point1
        # obj: point2
        if isinstance(obj, Point):
            return Point(self.__x + obj.x, self.__y + obj.y)
        elif isinstance(obj, int):
            return Point(self.__x + obj, self.__y + obj)

    def __sub__(self, obj):
        if isinstance(obj, Point):
            return Point(self.__x - obj.x, self.__y - obj.y)
        elif isinstance(obj, int):
            return Point(self.__x - obj, self.__y - obj)

    def __mul__(self, obj):
        if isinstance(obj, int):
            return Point(self.__x * obj, self.__y * obj)
    
    def __floordiv__(self, obj):
        # //
        pass

    def __truediv__(self, obj):
        # /
        pass

    def __mod__(self, obj):
        pass

    def __pow__(self, obj):
        pass


    # cast
    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __int__(self):
        # raise ValueError("Point object can't be casted to int")
        return self.__x + self.__y


point1 = Point(10, 10)
point2 = Point(20, 20)

# (10, 10)
# cast to string
# point1.__str__(), point2.__str__()
print(str(point1), str(point2))

# class property
print(Point._counts)

# int(point1), point1.__int__()
print(int(point1))

# add
# point1.+(point2)
# point1.__add__(point2)
print(point1 + point2)
print(point1 + 10)
# print(point1 + "ali")
# print(point1 + True)