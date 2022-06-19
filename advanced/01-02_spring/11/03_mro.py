class Animal:

    def __init__(self, name, species):
        self._name = name
        self._species = species
        print(f"[{self.__class__.__name__} | Animal]: __init__ is calling.")

    def fly(self):
        print(f"[{self.__class__.__name__} | Animal]: {self._name} | {self._species} is flying. ")

    def swim(self):
        print(f"[{self.__class__.__name__} | Animal]: {self._name} | {self._species} is swimming.")

    def move(self):
        print(f"[{self.__class__.__name__}| Animal]: {self._name} is moving.")

    # Now search in other parents
    # def asghar(self):
    #     print("Hello I am asghar in Animal.")


class Bird(Animal):

    def __init__(self, name):
        # self.__class__.__name__ => class name
        species = "Bird"
        print(f"[{self.__class__.__name__} | Bird]: __init__ is calling.")
        super(Bird, self).__init__(name, species)

    def fly(self):
        print(f"[{self.__class__.__name__} | Bird]: {self._name} is flying.")

    def swim(self):
        print(f"[{self.__class__.__name__}| Bird]: {self._name} is swimming")


class FlyableAnimal:

    def has_wings(self):
        print("Yes, it has.")

    def asghar(self):
        print("Hello I am asghar in FlyableAnimal.")


# parent
# mro - method resolution order
class Panguian(Bird, FlyableAnimal):
    # Constructor
    def __init__(self, name):
        print(f"[{self.__class__.__name__}]: __init__ is calling.")
        super().__init__(name)

    # @override - other language
    # override fly behaviour in parent
    def fly(self):
        print(f"[{self.__class__.__name__} | Panguian]: {self._name} can't fly.")


# bird = Bird("bird")
# pagu = Bird("pangu")
pagu = Panguian("pangu")
pagu.fly()
pagu.swim()
pagu.move()
pagu.asghar()