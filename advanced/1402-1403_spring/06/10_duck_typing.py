# Duck typing
# Dynmic type

class Sparrow:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")

    def swim(self):
        print(f"{self.name} is swimming.")


class Panguin:
    
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")

    def swim(self):
        print(f"{self.name} is swimming.")


class Duck:
    
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")

    def swim(self):
        print(f"{self.name} is swimming.")


obj1 = Duck(name="duck")
obj2 = Panguin(name="panguin")

obj1.swim()
obj2.fly()