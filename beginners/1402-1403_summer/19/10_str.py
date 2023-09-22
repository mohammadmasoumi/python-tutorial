
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):  # cast student instance to str
        return self.name

    def __int__(self):
        return 12


std1 = Student(name='asghar')
# <__main__.Student object at 0x000002417AF1E090>
print(std1)  # cast to str
print(str(std1))
print(int(std1))
# print(str(std1))
print(std1.name)
