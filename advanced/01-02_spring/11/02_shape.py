class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def p(self):
        return 2 * (self.x + self.y)

    @property
    def s(self):
        return self.x * self.y


class Square(Rectangle):

    def __init__(self, x):
        super().__init__(x, x)

    
square = Square(10)
print(square.x)
print(square.y)
print(square.s)
print(square.p)

rectangle = Rectangle(10, 20)
print(rectangle.x)
print(rectangle.y)
print(rectangle.s)
print(rectangle.p)

