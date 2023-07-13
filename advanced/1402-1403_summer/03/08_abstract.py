from abc import ABC, abstractmethod


class HumanAbstract(ABC):

    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def greeting(self):
        pass


# TypeError: Can't instantiate abstract class HumanAbstract with abstract method greeting
# instance = HumanAbstract(name="human1")

class AfricanHuman(HumanAbstract):

    def __init__(self, name):
        super().__init__(name)

    # def greeting(self):
    #     print(f"Hello, I am {self.name}")


# TypeError: Can't instantiate abstract class AfricanHuman with abstract method greeting
african1 = AfricanHuman(name='makumba')
# african1.greeting()
