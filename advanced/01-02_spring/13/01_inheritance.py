# inheritance

class Creature:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind 

    def move(self):
        print(f"[Parent] {self.name} is moving")

    def __str__(self):
        return f"{self.name}"


class Mamal(Creature):
    
    def __init__(self, name):
        super().__init__(name, "mamal")


    # def move(self):
    #     print(f"[Child] {self.name} is moving")

class Bird(Creature):
    
    def __init__(self, name):
        super().__init__(name, "bird")

    def move(self):
        print("i am printing")
        super().move()

        # print(f"[Child] {self.name} is flying")


# lion = Mamal(name="alex")
# print(lion)
# lion.move()


birdy = Bird(name="birdy")
print(birdy)
birdy.move()
print(birdy.kind)