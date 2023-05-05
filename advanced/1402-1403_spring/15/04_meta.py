
# name, bases, properties
# type()

class D:
    pass

class Metaclass(type):

    def __new__(cls, name, bases, properties={}):
        name += "Asghar"
        bases += (D, )
        properties = {"a": 12, **properties}

        instance = super(Metaclass, cls).__new__(cls, name, bases, properties)

        return instance


A = Metaclass("A", (), {})
B = Metaclass("B", (), {})
C = Metaclass("C", (A, B), {})


c = C()
print(C.__mro__)
print(c.a)