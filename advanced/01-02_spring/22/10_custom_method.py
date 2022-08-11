from enum import Enum

class Shape(Enum):
    RECTANGLE = "rect"
    TRIANGLE = "tri"
    CICLE = "circ"

    def describe(self):
        # "name: value"
        return f"{self.name}: {self.value}"

    @classmethod
    def fave_shape(cls):
        # cls: Shape
        # isntance: Shape.RECTANGLE
        # instance: cls.RECTANGLE
        # cls.RECTANGLE.value
        # cls.RECTANGLE.name
        return cls.RECTANGLE


print(Shape.RECTANGLE.describe())
print(Shape.fave_shape())