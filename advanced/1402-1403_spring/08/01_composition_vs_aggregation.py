# Composition VS Aggregation


class Wheel:
    pass


class Car1:
    
    def __init__(self, wheel):
        self.wheel = wheel

class Car2:

    def __init__(self):
        self.wheel = Wheel()


# aggregation
wheel = Wheel()
car1 = Car1(wheel=wheel)

# compostition
car2 = Car2()
