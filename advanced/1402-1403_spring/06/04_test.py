class A:
    pass

class B:
    def __init__(self, name):
        self.name = name

class C:
    pass

class D(A, B, C):
    pass


# CAOB
# CABO
c = D(name="asghar")
# dunder method
# magic function
print(D.__mro__)
