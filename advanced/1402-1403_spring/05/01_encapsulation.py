# Encapsulation

class Point:

    def __init__(self, x, y):
        # if x < 100:
        #     self.x = x
        # else:
        #     self.__x = x
        self.__x = x
        self.__y = y

    # get/read
    @property
    def x(self):
        return self.__x

    # set
    @x.setter
    def x(self, new_value):
        if new_value < 100:
            self.__x = new_value
    
    # delete
    @x.deleter
    def x(self):
        self.__x = 0
        # del self.__x

    # def mul(self):
    #     return self.x or self.__x

    def __str__(self):
        return f"({self.__x}, {self.__y})"


point1 = Point(10, 10)
print(point1)
# AttributeError: 'Point' object has no attribute '__x'
# print(point1.__x)
point1.x = 110
print(point1)

point1.x = 20
print(point1)