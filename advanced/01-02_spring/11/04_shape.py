import math

from rgwadmin import RGWAdmin

RGWAdmin()

class Shape:

    def __init__(self, color):
        self.color = color

    def what_is_your_color(self):
        print(f"{self.__class__.__name__} I am {self.color}")


class Circle(Shape):

    def __init__(self, radius, color):
        self.radius = radius
        super().__init__(color=color)

    @property
    def p(self):
        return 2 * self.radius * math.pi

    @property
    def s(self):
        return pow(self.radius, 2) * math.pi

class Rectangle(Shape):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        super().__init__(color=color)

    @property
    def p(self):
        return 2 * (self.x + self.y)

    @property
    def s(self):
        return self.x * self.y


class Square(Rectangle):

    def __init__(self, x, color):
        super().__init__(x, x, color)

    
square = Square(10, "red")
print(square.x)
print(square.y)
print(square.s)
print(square.p)
square.what_is_your_color()

rectangle = Rectangle(10, 20, "green")
print(rectangle.x)
print(rectangle.y)
print(rectangle.s)
print(rectangle.p)
rectangle.what_is_your_color()

circle = Circle(10, "blue")
print(circle.radius)
print(circle.s)
print(circle.p)
circle.what_is_your_color()
