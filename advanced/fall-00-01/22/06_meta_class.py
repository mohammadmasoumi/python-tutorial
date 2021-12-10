# prent A __call__
# A(a=1, b=2)
# __call__ metaclass (type)
# default metaclass type
#

class C:

    def test(self):
        print("Hello")


class D:
    pass


class MetaClass(type):
    #   type(name, (), {})
    def __new__(cls, name, bases, dct):
        print("Creating Instance in MetaClass")

        # parents
        bases = bases + (C,)
        print(f"[{name}] bases: {bases}")
        instance = super(MetaClass, cls).__new__(cls, name, bases, dct)

        return instance


class A(D, metaclass=MetaClass):

    # def __new__(cls, a, b):
    #     print("Creating Instance")
    #     # instance self
    #     self = super(A, cls).__new__(cls)
    #
    #     # inject instance
    #     self.properties = {}
    #
    #     return self

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.properties = {}


class B(metaclass=MetaClass):

    def __init__(self):
        pass


foo_1 = A(a=1, b=2)
foo_2 = B()

print(foo_1.a)
print(foo_1.b)
print(foo_1.test())
# print(foo_1.age)
# print(foo_1.last_name)
