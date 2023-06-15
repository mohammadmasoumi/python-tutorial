# inheritance
# وراثت


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} is speaking")

    def walk(self):
        print(f"{self.name} is walking.")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, "bird")

    def fly(self):
        print(f"{self.name} is flying.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat-sunan")

    def speak(self):
        print(f"{self.name} is meo meo nemio")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog-sunan")

    def speak(self):
        print(f"{self.name} is bark bark vagh")


class Parrot(Bird):
    def __init__(self, name):
        super().__init__(name)


tom = Cat("Tom")
tom.speak()
tom.walk()

# AttributeError: 'Cat' object has no attribute 'fly'
tom.fly()


fandogh = Parrot("fandogh")
fandogh.speak()  # Parrot -> parent Parrot -> parent parent Parrot
fandogh.fly()
