# __call__

class Student:

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"calling {self.name} with args: {args}, kwargs: {kwargs}")


radnia = Student(name='radnia')
# instance: radnia
# call instance of a class
radnia(12, score=2) # instance() -> instance.__class__.__call__()
