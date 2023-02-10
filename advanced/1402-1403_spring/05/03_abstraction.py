# Abstraction
# blueprint

from abc import ABC, abstractmethod

# blueprint
# incomplete 
# base class
class Animal(ABC):

    @abstractmethod
    def walk(self):
        pass

# derived 
# child
# مشتق شده
class Human(Animal):

    def __init__(self, name):
        self.name = name

    def walk(self):
        print("I am walking ...")


human1 = Human("human")
print(human1)

# class Cell:

#     def get_cell(self):
#         pass


# class Bomberman:

#     def bomb(self):
#         pass
