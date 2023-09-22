
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


# ["asghar", "ali"]
# create instance
# Student() -> Student.init()
#                keyword args
std1 = Student(name="ali", height=190, weight=90, age=22)  # Student.init(std1)
# std1 = Student(height=190, weight=90, age=22, name="ali")
# positional args
# Student.__init__() takes 5 positional arguments but 6 were given
# std2 = Student("asghar", 200, 100, 19, 200)
# Student.init(std2, "asghar", 200, 100, 19)
std2 = Student("asghar", 200, 100, 19)

# access to property
# variable.[property name]
print(std1.name)
print(std2.name)
# print(std1.age)
# print(std1.height)
# print(std1.weight)
