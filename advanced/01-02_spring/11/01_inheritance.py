class Creature:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def move(self):
        print(f"[{self.__class__.__name__} | Creature] {self.name} am moving.")

    def __str__(self) -> str:
        return f"{self.name}"
        

class Mamal(Creature):

    SPECIES = "mamal"

    def __init__(self, name):
        super().__init__(name, self.SPECIES)


class Bird(Creature):

    SPECIES = "Bird"

    def __init__(self, name):
        super().__init__(name, self.SPECIES)


    def move(self):
        print(f"[{self.__class__.__name__} | Bird] {self.name} am flying.")
        
        # call parent method
        return super().move()


lion = Mamal("alex")
lion.move()

owl = Bird("night-vision")
owl.move()