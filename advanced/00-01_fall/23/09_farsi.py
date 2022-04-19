class MyString:

    def __init__(self, name):
        self._name = name

    def __add__(self, other):
        return self._name + other._name

    __mul__ = __add__

    # def __mul__(self, other):


name1 = MyString("ali")
name2 = MyString("hassan")

print(name1 + name2)
print(name1 * name2)
