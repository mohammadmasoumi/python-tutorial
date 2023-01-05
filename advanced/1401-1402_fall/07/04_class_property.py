
class Student:
    STUDENTS = []

    def __init__(self, name, avg) -> None:
        self.name = name
        self.avg = avg

        Student.STUDENTS.append(self)

    @classmethod
    def get_total_avg(cls):
        avg_list = [item.avg for item in cls.STUDENTS]
        return sum(avg_list) / len(avg_list)

    @classmethod
    def get_students_name(cls):
        return [student.name for student in cls.STUDENTS]

std1 = Student("maryam", 20)
std2 = Student("asghar", 10)

print(Student.get_total_avg())
print(Student.get_students_name())