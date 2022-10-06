"""

class type:

    def __call__(cls, *args, **kwargs):
        self = cls.__new__(cls, *args, **kwargs)
        cls.__init__(self, *args, **kwargs)

class A:
    def __init__(self, age):
        self.age = age

    def __call__(self, *args, **kwargs):
        pass


A = type("A", (), {})
a = A(age=12)
print(a())


"""

class A:
    def __new__(cls, a, b):
        print("Creating Instance 1")
        # instance self
        self = super(A, cls).__new__(cls)

        # inject instance
        self.properties = {}
        self.asghar = "asghar"

        return self

    def __init__(self, a, b):
        print("Creating Instance 2")
        self.a = a
        self.b = b
        # self.properties = {}


foo_1 = A(a=1, b=2)
# foo_2 = A(a=1, b=3)

print(foo_1.a)
print(foo_1.b)
print(foo_1.properties)
print(foo_1.asghar)
# print(foo_1.age)
# print(foo_1.last_name)