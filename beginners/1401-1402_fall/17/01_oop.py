# snake_case
# PascalCase
# camelCase

# PascalCase
class Student:

    # constructor
    # __functionname__
    # dunder method or magic function
    def __init__(self, name, my_age, school="ShahidSattari"):
        # current object
        # self.attribute
        # self.property
        # self.[attribute_name]
        self.age = my_age
        self.firstname = name
        self.school = school
        # self.lesson = None
        # self.lesson = lesson

    def study(self, lesson):
        # self.lesson = lesson
        print(f"{self.firstname} is studying {lesson} ... ")


# Student(name="mina", my_age=22)
# Student(mina, name="mina", my_age=22)
mina = Student(name="mina", my_age=22)
student = Student("hadi", 22)

print(Student(name="ahmad", age=22).name)
std = Student(name="ahmad", age=22)
print(std.name)
print(mina)
print(mina.firstname, student.firstname)
print(mina.age, student.age)

# study(mina)
# instance.behaviour_name()
mina.study("math")
mina.study("art")
print(f"{mina.firstname} is studying {'art'} ... ")
print(f"{student.firstname} is studying {'science'} ... ")

student.study("scinece")
