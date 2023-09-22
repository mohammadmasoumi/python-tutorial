# helper function
def define_new_prop(a):
    pass


class Student:
    # sth
    # dunder method or magic function
    # preserve method

    # constructor
    #                        params
    """
    {
        "name": "ali",
        "height": 190,
        "weight": 90,
        "age": 22,
    }
    ==> []
    """

    def __init__(self, name, height, weight, age):
        # self: current instance
        # self: std1
        # self: std2

        # AttributeError: 'Student' object has no attribute 'name'
        # print(self.name)

        # define property for instance
        # self.[property name]
        # property name  = value
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

        # print(self.name)

        # self.walk = lambda self: print("{self.name} is walking.")

    # helper method on class
    def define_new_prop(self):
        self.new_property = "test"  # Do not try this at home.

    def dosth(self):
        # std1.walk() => self.walk()
        self.walk()
        self.study("science")
        # AttributeError: 'Student' object has no attribute 'new_property'
        print(self.new_property)

    # behaviour -> method | call
    def walk(self):  # self: std1
        # self.name
        # std1.name
        # std2.name
        print("{self.name} is walking.")

    def study(self, lesson):
        print(f"{self.name} is studying {lesson}.")
        return 20


# ["asghar", "ali"]
# create instance
# Student() -> Student.init()
#                keyword args
std1 = Student(name="ali", height=190, weight=90, age=22)  # Student.init(std1)
# std1 = Student(height=190, weight=90, age=22, name="ali")
# positional args
std2 = Student("asghar", 200, 100, 19)  # Student.init(std2)

# access to property
# variable.[property name]
print(std1.name)
print(std2.name)
# print(std1.age)
# print(std1.height)
# print(std1.weight)

std1.walk()  # Student.walk(std1)
std2.walk()  # Student.walk(std2)

result = std1.study(lesson="math")
std2.study("litreture")

print(result)
std1.define_new_prop()
std1.dosth()
# AttributeError: 'Student' object has no attribute 'new_property'
std2.dosth()
