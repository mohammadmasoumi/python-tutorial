

class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking ...")


class Human(Animal):

    def __init__(self, name, age):
        super().__init__(name)
        # self.name = name
        self.age = age

    def walk(self):
        super().walk()
        print(f"[Child]{self.name} is walking ...")




animal = Animal("lion")
animal.walk()

human1 = Human("human", 21)
human1.walk()


# class Fish(Human):

#     def __init__(self, name, age):
#         super().__init__(name, age)