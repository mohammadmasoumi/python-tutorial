from datetime import datetime 

class Student:

    def __init__(self, name, birth) -> None:
        self.name = name
        self.birth = birth

    @property
    def age(self):
        year, month, day = map(int, self.birth.split("-"))
        print(f"year: {year}, month: {month}, day: {day}")

        return (datetime.utcnow() - datetime(year=year, month=month, day=day)).days // 365


# PEP
std1 = Student(name="Alireza", birth="1997-12-12")
print(std1.name)
print(std1.age)
