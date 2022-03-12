class Base:

    def __init__(self, name, age):
        # _name is a private property but you can access it from outside
        self._name = name
        # __age is a private property and you can not access it from outside
        self.__age = age


class Derived(Base):

    def __init__(self, name, age):
        super().__init__(name, age)
        # Base.__init__(self, name, age)


derived = Derived("ali", 20)
print(derived._name)
# AttributeError: 'Derived' object has no attribute '__age'
print(derived.__age)