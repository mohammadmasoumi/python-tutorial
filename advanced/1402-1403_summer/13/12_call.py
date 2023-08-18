# __call__

class Metaclass(type, metaclass=type):

    # def __init__(self, name, bases, d):
    #     pass

    def __new__(cls, name, bases, d):
        instance = super().__new__(cls, name, bases, d)
        return instance

    def __call__(cls, *args, **kwargs):
        # print(self)
        # print(args, kwargs)
        
        self = cls.__new__(cls, *args, **kwargs)
        cls.__init__(self, *args, **kwargs)

        return self

class Student(metaclass=Metaclass):

    def __init__(self, name):
        self.name = name

    def __new__(cls, name):
        self = super(Student, cls).__new__(cls)
        self.age = 22
        return self

    def __call__(self, *args, **kwargs):
        print(f"calling {self.name} with args: {args}, kwargs: {kwargs}")


print(isinstance(Student, Metaclass)) # True

# Student is an instance of Metaclass
# Student() -> Metaclass.__call__
# instance() -> parent.__call__

radnia = Student(name='radnia')
# instance: radnia
# call instance of a class
radnia(12, score=2) # instance() -> instance.__class__.__call__()
