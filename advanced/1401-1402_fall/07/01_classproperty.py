

"""
                    - instance level -> name, students
        - property 
                    - class level -> STUDENTS
Concept: 
                    - instance level -> study
        - behavior
                    - class level -> get_students


class level -> [property & behavior] class level

"""

class Student:
    students = []

    def __init__(self, name) -> None:
        self.name = name
        # self.students = []
        Student.students.append(self.name)

    @classmethod
    def get_cls_name(cls):
        # cls: Student
        # cls.get_cls_name()
        # clas.students
        # Student.get_cls_name()
        # cls.get_cls_name()
        print(f"cls: {cls}")
        return str(cls)

    @classmethod
    def get_list_of_students(cls):
        return cls.students

    def __str__(self) -> str:
        return self.name


std1 = Student("ali")
# print(std1.students)
print(Student.get_cls_name())
print(Student.get_list_of_students())

std2 = Student("mohammad")
print(Student.get_cls_name())
print(Student.get_list_of_students())
# print(std2.students)
