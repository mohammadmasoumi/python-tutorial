import math
# Circle, Square, Rectangle, Trianble


class Shape:
    SPECIES = None

    def __init__(self, colour):
        print(f"self: {self}, type: {type(self)}")

        self.species = self.SPECIES
        self.colour = colour


class Circle(Shape):
    SPECIES = 'Circle'  # class property

    def __init__(self, colour, radius):
        super().__init__(colour=colour)
        self.radius = radius

    def p(self):
        return 2 * self.radius * math.pi

    def s(self):
        return (self.radius ** 2) * math.pi


class Rectangle(Shape):
    SPECIES = 'Rectangle'

    def __init__(self, colour, height, width):
        super().__init__(colour=colour)
        self.height = height
        self.width = width

    def p(self):
        return 2 * (self.height + self.width)

    def s(self):
        return self.height * self.width


class Square(Rectangle):
    SPECIES = 'Square'

    def __init__(self, colour, side):
        super().__init__(colour=colour, height=side, width=side)


class Triangle(Shape):
    SPECIES = 'Triangle'

    def __init__(self, colour, side):
        super().__init__(colour)
        self.side = side

    def p(self):
        return 3 * self.side

    def s(self):
        h = math.sqrt(3) / 2 * self.side
        return (h * self.side) // 2


# --------------
p1 = Shape('black')
c1 = Circle('red', 2)

shapes = [
    Circle('red', 2),
    Circle('blue', 3),
    Rectangle('yellow', height=10, width=5),
    Triangle('dark', 3),
    Square('purple', side=10)
]

for shape in shapes:
    print(f"[{shape.SPECIES}]: masahat: {shape.s()}")
    print(f"[{shape.SPECIES}]: mohit: {shape.p()}")
