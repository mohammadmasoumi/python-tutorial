print(type(type))

#    "name", "bases", "properties"
A = type("A", (), {"a": 12})
# (12, )
#      string  tuple dict
B = type("B", (), {"a": 13})
C = type("C", (A, B), {"a": 14})
D = type("D", (C, ), {"a": 15})

print(D.__mro__)

delattr(D, "a") # class property
d = D()
print(d.a)

# delattr(d, "a")
print(getattr(d, "a"))
print(dir(d))
# delattr(d, a)

# del d.a
# print(d.a)

class D(C):
    # classproperty
    a = 15

class Student:

    def __init__(self, name):
        self.name = name


std1 = Student(name="ali")
delattr(std1, "name")
# print(std1.name)


