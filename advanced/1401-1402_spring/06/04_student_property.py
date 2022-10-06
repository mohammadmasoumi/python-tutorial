# naming convention
# 1. snake case [variables, methods]
# 2. camel case
# 3. pascal case [class name]
# keyword: class

from datetime import datetime, timedelta

class Student:

    # constructor
    def __init__(self, student_name, student_birthday, student_gender):
        # self: currenct instance 
        # 1996-03-02
        # ["1996", "03", "02"]

        # year_month_day = list(map(int, student_birthday.split("-")))
        # age = (datetime.utcnow() - datetime(
        #     year=year_month_day[0], 
        #     month=year_month_day[1], 
        #     day=year_month_day[2]
        # )).days // 365

        # attribute
        self.name = student_name
        self.birthday = student_birthday
        self.gender = student_gender
        self.scores = []

    # behaviour
    def walk(self):
        # attribute:
        #   name
        #   age
        #   gender
        #   scores
        # behaviour:
        #   walk
        print(f"[{self.name}]:I am walking")

    @property
    def age(self):
        # no inputs
        year_month_day = list(map(int, self.birthday.split("-")))
        return (datetime.utcnow() - datetime(
            year=year_month_day[0], 
            month=year_month_day[1], 
            day=year_month_day[2]
        )).days // 365


student1 = Student("Asghar", "1996-03-02", "male")
# print(student1.age())
# تبدیل یک رفتار به ویژگی
# 
print(student1.age)