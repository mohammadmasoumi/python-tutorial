"""
Composition (is a)
 - HEART is a part of body
 - ENGINE is a part of car 

You can't separate two objects from each other.

HEART, HUMAN


Aggregation (has a )
 - Imani has a Cap
 - Sabour has a watch
 - Eskandari has a necklace

"""

# Composition


class Heart:
    def __init__(self):
        pass


# Aggregation

class Cap:
    def __init__(self, colour):
        self.colour = colour


class Human:

    def __init__(self, name, cap):
        self.name = name
        self.cap = cap  # Aggregation
        self.heart = Heart()  # Composition


# Dependency injection
cap1 = Cap('red')
imani = Human('imani', cap=cap1)
