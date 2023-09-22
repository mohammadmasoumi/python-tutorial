
class Student:
    # __sth__
    # dunder method or magic function
    # preserve method

    # constructor
    def __init__(self):
        # self: current instance
        # self: std1
        # self: std2

        # AttributeError: 'Student' object has no attribute 'name'
        # print(self.name)

        # define property for instance
        # self.[property name]
        self.name = "ali"
        self.height = 190
        self.weight = 90
        self.age = 22

        print(self.name)


# create instance
# Student() -> Student.__init__()
std1 = Student()  # Student.__init__(std1)
std2 = Student()  # Student.__init__(std2)

# access to property
# variable.[property name]
print(std1.name)
print(std2.name)
print(std1.age)
print(std1.height)
print(std1.weight)

print(id(std1), id(std2))
