import math


class Shape:

    def __init__(self, name, color):
        self.name = name
        self.color = color


class Circle(Shape):

    def __init__(self, name, color, radius):
        super().__init__(name=name, color=color)
        self.radius = radius

    def p(self):
        return 2 * math.pi * self.radius

    def s(self):
        return pow(r, 2) * math.pi


class Rectangle(Shape):

    def __init__(self, name, color, width, length):
        super().__init__(name=name, color=color)
        self.width = width
        self.length = length

    def p(self):
        return 2 * (self.width + self.length)

    def s(self):
        return self.width * self.length


class Square(Rectangle):

    def __init__(self, name, color, width):
        super().__init__(name, color, width, width)


circle1 = Circle(name="circle", color="red", radius=1)
print(circle1.p())

rectange = Rectangle("rectangle", "black", 10, 20)
print(rectange.p())

square = Square("rectangle", "black", 10)
print(square.p())
