# cat
# name
# greet -> My name is {}
# speak -> Meo Meo

class Cat:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"My name is {self.name}")
        # return
        # return None

    def speak(self):
        print("Meo Meo ...")


tom1 = Cat(name="tom")
tom2 = Cat("tom")

print(tom1.name)
print(tom1.greet())
tom1.speak()
