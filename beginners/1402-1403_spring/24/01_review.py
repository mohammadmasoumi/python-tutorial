
class Student:

    # method: __init__
    # __sth__: dunder method or magic function
    # __init__ -> constructor
    # __str__ -> cast to str
    # __int__
    # __float__
    # __ceil__
    # __floordiv__
    # __truediv__
    # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__',
    #'__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__',
    #'__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__',
    #'__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__',
    #'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
    #'__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__',
    #'__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__',
    #'__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__',
    #'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length',
    # 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

    def __init__(self, name):  # params
        # self: current object

        # Concepts in OOP
        #  - property - variable
        #       - name
        #       - age
        #       - degree
        #       - grade
        #       - height
        #       - weight
        #       - width
        #       - health
        #  - behaviour - method
        #       - study()
        #       - walk()
        #       - sleep()
        #       - eat()
        #       - wakeup()
        #       - play()
        #       - live()
        # self.property = value
        self.name = name
        self.firstname = name
        self.age = 20

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    """
    DO NOT EXIST IN PYTHON

    method overloading
    - def study(self):
        print(f"{self.name} is studing ...")

    - def study(self, course):
        print(f"{self.name} is studying {course}")
    
    std1.study()
    std1.study('math')
    """

    def study(self):
        # self: std1
        # self: std2
        # current object
        print(f"{self.name} is studying")

    def study(self, course):
        print(f"{self.name} is studying {course}")


# a = 12
# a = 13

# TypeError: Student.__init__() missing 1 required positional argument: 'age'
std1 = Student('asghar')  # -> Student.__init__(name='asghar')
print(std1.name)
print(std1.age)
std1.study('math')  # study(std1)

std2 = Student('mona')
std2.study('science')  # study(std2)
print(std2.age)
