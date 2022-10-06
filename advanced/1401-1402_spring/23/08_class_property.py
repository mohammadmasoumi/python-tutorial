

class ClassPropertyDescriptor:

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def setter(self, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self

def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)

    return ClassPropertyDescriptor(func)


class Person:
    # class property
    # COUNT = 0

    # @peroprty
    # def age(self):
    #     pass

    @classproperty
    def count(cls):
        return 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

        # instance property
        # self.COUNT += 1

        # class property
        Person.count += 1


person1 = Person('Asghar', 22)
person2 = Person('Akbar', 22)

# print(person1.count)
print(Person.count)