# inheritance: creating new class from an existing one.
# multiple inheritance
class Creature:

    def __init__(self) -> None:
        print("Creature is ready")

    def whoisthis(self):
        print("This is a creature")

    def eat(self):
        print("Creature is eating.")


class Animal(Creature):
    species = "Animal"

    def __init__(self) -> None:
        super().__init__()
        print("Animal is ready")

    def whoisthis(self):
        print("This is an animal")

    # def eat(self):
    #     print("Animal is eating.")


class EggableAnimal:

    def breed(self):
        print("Making egg.")

    def eat(self):
        print("EggableAnimal is eating.")


# mro - method resolution order
# left to right
class Bird(Animal, EggableAnimal):

    # class property
    # این ویژگی بین همه نمونه های یکسان است
    # peggy and ostrich and ... each of them has species and the value is the same
    species = "Bird"

    def __init__(self) -> None:
        super().__init__()
        print("Bird is ready")

    def whoisthis(self):
        print("This is a bird")

    def swim(self):
        print("Swim faster")

    def fly(self):
        print("Bird is flying.")


class Panguin(Bird):
    # constructor
    def __init__(self) -> None:
        # super(): acess to the parent element(behaviour and properties)
        # به رفتارها و ویژگی های پدر دسترسی پیدا میکنید
        super().__init__()
        print("Panguin is ready")

    def whoisthis(self):
        # super().behaviour()
        super().whoisthis()
        super().swim()
        print("This is a panguin")

    def run(self):
        print("Run faster")


class Ostrich(Bird):

    def __init__(self) -> None:
        super().__init__()

    def whoisthis(self):
        # super().whoisthis()
        print("This is ostrich")

    # override - fly behaviour
    def fly(self):
        print("Ostrich can not fly.")


peggy = Panguin()
peggy.whoisthis()
peggy.run()
peggy.swim()
peggy.eat()
print(peggy.species)

ostrich = Ostrich()
ostrich.whoisthis()
ostrich.fly()
print(ostrich.species)
