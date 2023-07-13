class A:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello, My name is {self.name}!")


class B:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello, My name is {self.name}!")

    def bye(self):
        pass


a1 = A(name="a1")
a2 = A(name="a2")

b1 = B(name="b1", age=20)
b2 = B(name="b2", age=20)

a_and_b_s = [a1, b1, a2, b2]

for item in a_and_b_s:
    print(item.greeting())
