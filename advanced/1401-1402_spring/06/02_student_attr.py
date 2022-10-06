# naming convention
# 1. snake case [variables, methods]
# 2. camel case
# 3. pascal case [class name]
# keyword: class

class Student:

    # constructor
    def __init__(self, student_name, student_age, student_gender):
        # self: currenct instance 

        # attribute
        self.name = student_name
        self.age = student_age
        self.gender = student_gender
        self.scores = []


# Student.__init__(student1, student_name="Ali", student_age=12, student_gender="male")

# create an instance
student1 = Student(student_name="Ali", student_age=12, student_gender="male")
student2 = Student(student_name="Asghar", student_age=2, student_gender="male")

# instance_name.attribute
print(student1.name)
print(student1.age)
print(student1.gender)
print(student2.name)