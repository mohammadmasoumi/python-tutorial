# abstract - انتزاع

from abc import ABC, abstractmethod


# abstract class
class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Bird(Animal):
    species = "Bird"

    def __init__(self, name):
        self.__name = name

    def move(self):
        print("I am flying.")
    
    def eat(self):
        print("I am eating.")


class Mamal(Animal):
    species = "Mamal"

    def __init__(self, name):
        self.__name = name

    def move(self):
        print("I am running.")
    
    def eat(self):
        print("I eat meat.")


# you can not create instance from abstract class
# TypeError: Can't instantiate abstract class Animal with abstract methods eat, move
# animal = Animal()
# از خود قالب نمیتوانم نمونه بسازم

# TypeError: Can't instantiate abstract class Bird with abstract methods eat, move
bird = Bird("canary")
bird.move()    
    