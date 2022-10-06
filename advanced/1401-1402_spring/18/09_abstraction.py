from abc import ABC, abstractmethod


class AnimalInterface(ABC):
    
    @abstractmethod
    def move(self, direction):
        pass

    @abstractmethod
    def eat():
        pass


class Bird(AnimalInterface):
    
    def __init__(self, name) -> None:
        self.name = name

    def move(self, direction):
        print(f"I am moving to {direction}!")
        # return self

    def eat(self):
        print("I am eating.")

    def swim(self):
        print("I am swiming.")

    def __str__(self) -> str:
        return f"{self.name}"


class Birt2(Bird):
    pass


# TypeError: Can't instantiate abstract class AnimalInterface with abstract methods eat, move
# interface = AnimalInterface()

bird = Bird("asghar")
print(bird)
bird.move("right")
bird.swim()

bird2 = Birt2("akbar")
print(bird2)


