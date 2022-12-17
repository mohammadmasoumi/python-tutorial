
class Student:

    def __init__(self, name):
        self.name = name
        self.grade = 19


std1 = Student("mina")
print(std1.name)
print(std1.grade)
std1.grade = -1
print(std1.grade)

