# class property

class Student:
    # class property
    STUDENT_NUMBERS = 0
    STUDENTS = []

    # instance property
    std_number = 0

    def __init__(self, name, birthday):
        self.__name = name
        self.__birthday = birthday

        # instance level property
        self.std_number += 1

        # class level property
        Student.STUDENT_NUMBERS += 1
        Student.STUDENTS.append(self)

    def __str__(self):
        return self.__name

# Count of students?
std1 = Student(name="Ali", birthday="1998-10-20")
std2 = Student(name="Hossein", birthday="2000-10-20")
std3 = Student(name="asghar", birthday="2000-10-20")

print(Student.STUDENT_NUMBERS)
print(Student.STUDENTS)

for std in Student.STUDENTS:
    print(std)


