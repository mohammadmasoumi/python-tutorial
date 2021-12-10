# prent A __call__
# A(a=1, b=2)
# __call__ metaclass (type)
# default metaclass type
#
"""
metaclass type

    def __call__(a, b)
        obj = A.__new__(cls, a, b)
        # obj: None
        __init__(obj, a, b)

"""


class A:

    def __new__(cls, a, b):
        print("Creating Instance")
        # instance self
        self = super(A, cls).__new__(cls)

        # inject instance
        self.properties = {}

        return self

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.properties = {}


foo_1 = A(a=1, b=2)
foo_2 = A(a=1, b=3)

print(foo_1.a)
print(foo_1.b)
# print(foo_1.age)
# print(foo_1.last_name)
