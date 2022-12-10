
class Student:

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, lesson):
        print(f"{self.name} is studying {lesson}")


print(Student("maryam", 22).study("art"))

# Student.__init__("mina", 22)
std1 = Student("mina", 22)
std1.study("math")

std2 = Student("hadi", 22)
std2.study("math")
