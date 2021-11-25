# Abstraction


"""
1. Encapsulation
    private method
    private property
    _, __

2. Abstraction: انتزاعی
"""

from abc import ABC, abstractmethod


class AnimalInterface(ABC):

    # def move(self):
    # raise NotImplemented

    # @abstractproperty
    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def move1(self):
        pass

    @abstractmethod
    def move2(self):
        pass

    @abstractmethod
    def move3(self):
        pass


class Cat(AnimalInterface):
    """
    alt + insert
    ctrl + i
    shift + bottom arrow
    """

    @property
    def age(self):
        return 12

    def move1(self):
        print("move1")

    def move2(self):
        print("move2")

    def move3(self):
        print("move3")


class Dog(AnimalInterface):

    def age(self):
        pass

    def move1(self):
        pass

    def move2(self):
        pass

    def move3(self):
        pass


# TypeError: Can't instantiate abstract class AnimalInterface with abstract methods move1, move2, move3
# animal = AnimalInterface()
# print(animal)

cat = Cat()
cat.move1()
print(cat.age)
