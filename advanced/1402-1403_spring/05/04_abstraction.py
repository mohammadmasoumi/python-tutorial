# Abstraction
# blueprint

from abc import ABC, abstractmethod, abstractproperty, abstractstaticmethod, abstractclassmethod

# blueprint
# incomplete 
# base class
class Animal(ABC):

    @abstractproperty
    def race(self):
        pass

    # incomplete method
    @abstractmethod
    def walk(self):
        print("I am walking yoouuuuuha!")

    # normal method
    # concrete method
    def swim(self):
        print("i am swimming")


# derived 
# child
class Human(Animal):

    def __init__(self, name):
        self.name = name

    @property
    def race(self):
        return "Mammal"

    # TypeError: Can't instantiate abstract class Human with abstract method walk
    def walk(self):
        super().walk()
        print("I am walking ...")


# TypeError: Can't instantiate abstract class Animal with abstract method walk
# animal = Animal()

human1 = Human("human")
print(human1)
human1.walk()
human1.swim()

