# multiple inheritance

class Animal:

    def __init__(self, name, species):
        print(f"[{self.__class__.__name__}]: creating animal.")
        self.name = name
        self.species = species

    def move(self):
        print(f"[{self.__class__.__name__} Animal]: I am moving.")

    def swinm(self):
        print(f"[{self.__class__.__name__} Animal]: I am swiming.")
    
    # def fly(self):
    #     print(f"[{self.__class__.__name__} Animal]: I am flying.")



class Bird(Animal):
    species = "Bird"
    counter = 0

    def __init__(self, name):
        print(f"[{self.__class__.__name__}]: creating bird.")
        Bird.counter += 1
        super().__init__(name, Bird.species)

    def swinm(self):
        print(f"[{self.__class__.__name__} Bird]: I am swiming.")

    # def fly(self):
    #     print(f"[{self.__class__.__name__} Bird]: I am flying.")


class FalyableAnimal:

    def has_wings(self):
        print("Yes")

    def fly(self):
        print(f"[{self.__class__.__name__} FalyableAnimal]: I am flying.")



class Panguian(Bird, FalyableAnimal):
    # mro
    # method resolution order

    def __init__(self, name):
        # self.name = name
        print(f"[{self.__class__.__name__}]: creating panguain.")
        super().__init__(name)

    # def fly(self):
    #     print(f"[{self.__class__.__name__}]: I am flying.")


pangu = Panguian("pangu")
pangu.fly()
pangu.has_wings()
print("--------------------------")
# bird = Bird("bird")
# bird.fly()

# Panguian("asghar")
# pangu.__class__("asghar")
# pangu.__class__.__name__