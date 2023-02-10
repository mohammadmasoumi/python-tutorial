# HAS A

"""
Composition:
    Two entities are related to each other. (Dependent)
    PART OF

 - Human has a heart. HEART is PART OF a HUMAN
 - Panguin has feet.
 - Panguin has wings.

Aggregation:
    Two entities are independent and can separate them.

 - Department has students.
 - Mr. Shasti has a Car.
 - Mr. Shasti has a Cap.

"""

# Composition [Concept]


class Heart:
    pass


class Human:

    def __init__(self, name):
        self.name = name
        self.heart = Heart()


human = Human(name="asghar")
# Aggregation [Concept]
# Dependency injection [Pattern]


class Car:
    pass


class MrShasty:

    def __init__(self, car):
        self.car = car


car = Car()
shasty = MrShasty(car=car)
