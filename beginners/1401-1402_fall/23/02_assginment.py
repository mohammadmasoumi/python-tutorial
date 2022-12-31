
class Student:
    STUDENTS = []

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        Student.STUDENTS.append(self)

    def study(self, lesson):
        print(f"{self.name} is studying {lesson}")

    @classmethod
    def get_class_grade(cls):
        print(cls.STUDENTS)

        # grades = []
        # for student in cls.STUDENTS:
        #     grades.append(student.grade)

        grades = [student.grade for student in cls.STUDENTS]

        # ZeroDivisionError: division by zero
        return sum(grades) / len(grades) if len(grades) else 0

    @classmethod
    def study_all(cls):
        for student in cls.STUDENTS:
            student.study("math")


print(Student.get_class_grade())

std1 = Student("ali1", 20)
std2 = Student("ali2", 20) 

# STUDENTS: [std1, std2]

print(Student.get_class_grade())
print([std1, std2])

Student.study_all()