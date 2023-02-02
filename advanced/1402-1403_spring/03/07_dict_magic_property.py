
class A:
    def __init__(self):
        self.name = "asghar"
        self.age = 22

    def f(self, a):
        return a


# property and function
print(A.__dict__)
print(A().__dict__)
