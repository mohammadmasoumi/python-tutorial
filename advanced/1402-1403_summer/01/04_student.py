class Student:

    def __init__(self, name, pos, height=170):
        self.name = name
        self.pos = pos
        self.height = height

    def change_name(self, new_name):
        self.name = new_name
        print(f"My name is {self.name}")

    # behaviour: self
    # instance behaviour
    def walk(self):
        # self: current
        # access: print(self.pos), self.pos
        print(f"I am in the {self.pos} position.")
        # self.pos = self.pos + 1
        self.pos += 1
        print(f"My new position is {self.pos}.")


std1 = Student(name="asghar", pos=1)
std1.walk()  # behaviour
std1.change_name("Asghar")
#
# print(std1.name) [access, read]
# std1.name = "new value" [update]
# del std1.name [delete]
std1.name = "akbar"
print(std1.name)

std2 = Student(name="akbar", pos=1)
std2.walk()
