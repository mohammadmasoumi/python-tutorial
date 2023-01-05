

"""
                    - instance level
        - property 
                    - class level
concept: 
                    - instance level
        - behavior
                    - class level


class level -> [property & behavior] class level

"""


class Student:

    STUDENTS = []

    def __init__(self, name) -> None:
        # CURRENT OJB: self
        # self: std1
        # self: std2

        # instance property

        # name: "ali"
        # self: std1

        # std1.name: "ali"
        # std1.students: []
        # std1.students: ["ali"]

        # name: "mohammad"
        # self: std2

        # std2.name: "mohammad"
        # std2.students: []
        # std2.students: ["mohammad"]

        self.name = name
        self.students = []
        # self.students.append(self)
        self.students.append(self.name)

        # instance property
        # [self].[property name]

        # class property
        # [cls].[property name]
        Student.STUDENTS.append(self.name)

    def study(self, lesson):
        # instance behavior
        print(f"{self.name} is studying {lesson}.")

    @classmethod
    def get_students(cls):
        # cls: Student
        return cls.STUDENTS


std1 = Student(name="ali")
# instance property
print(std1.students)  # ["ali"]
std1.study("math")
# class property
print(Student.STUDENTS)  # ["ali"]
print(Student.get_students())

std2 = Student(name="mohammad")
# instance property
print(std2.students)  # ["mohammad"]
std1.study("art")
# class property
print(Student.STUDENTS)  # ["ali", "mohammad"]
print(Student.get_students())
