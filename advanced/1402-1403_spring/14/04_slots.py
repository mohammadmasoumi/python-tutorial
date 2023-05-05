
class A:
    # defining the slots
    __slots__ = ('a', 'b')

    def __init__(self, a, b):
        # initializing the values
        self.a = a
        self.b = b


print(A.__dict__)
