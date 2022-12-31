

# instance
"""
                                                - instance
        - property/attribute [height, age, name] 
                                                -class level
Concept: 
                                                - instance
        - behavior [study, eat]
                                                - class level

"""

class Student:

    students = []

    def __init__(self, name, grade):
        # self: std1
        # name: "ali"
        # grade: 10
        # std1.name = "ali"
        # std1.grade = 10

        # self: std2
        # name: "mobina"
        # grade: 20
        # std1.name = "mobina"
        # std1.grade = 20

        self.name = name
        self.grade = grade

        # std1.students = []
        # std2.students = []
        # self.students = []

        Student.students.append(self.name)
        # cls: Student

        # self.students.append(self)
        # self.students.append(self.name)
        # std1.students = ["ali"]
        # std2.students = ["mobina"]

    @classmethod
    def get_students_name(cls):
        # Student.
        # cls.
        return cls.students

    @classmethod
    def add_students(cls, std):
        cls.students.append(std.name)


# students = []
print(Student.students)
print(Student.get_students_name())

std1 = Student(name="ali", grade=10)
print(std1.name)
print(std1.grade)
print(std1.students) # ["ali"]
print(Student.students)
print(Student.get_students_name())

std2 = Student("mobina", 20)
print(std2.name)
print(std2.grade)
print(std2.students)
print(Student.students)
print(Student.get_students_name())

print(Student.add_students(std2))
print(Student.get_students_name())



