from enum import Enum

class Shape(Enum):
    RECTANGLE = "rect"
    TRIANGLE = "tri"
    CICLE = "circ"


# ordered
for shape in Shape:
    print(shape.name, shape.value)

