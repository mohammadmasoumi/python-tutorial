"""
object
def __call__(cls, *args, **kwrags):
    self = cls.__new__(cls, *args, **kwrags)
    cls.__init__(self, *args, **kwrags)

A()
"""

class A:

    def __new__(cls, name, age):
        print("__new__")
        # instance self
        self = super(A, cls).__new__(cls)

        # inject instance
        self.properties = {}
        self.name = name + "mamad"

        return self

    def __init__(self, name, age):
        print("__init__")
        self.name = name
        self.age = age

a = A("asghar", 12)

print(a.name)
print(a.age)
# print(a.custom_name)
print(a.properties)