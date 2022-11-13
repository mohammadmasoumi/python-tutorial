# object oriented programmin
# OOP
from datetime import datetime, timedelta
# object

# attribute/property -> datatype (str, int, float, list, dict, set, tuple, ...)
# behaviour -> method

# className => PascalCase


class Student:

    # constructor
    # __function_name__
    # magic function or dunder method
    # __init__
    def __init__(self, name, birth_date):
        # self: current object
        # property
        # self.[propertyname] = value
        # attribute:
        #   - name
        #   - firstname
        #   - asghar
        # student1.name = name
        # student1.firstname  = name
        self.name = name
        self.firstname = name
        self.asghar = name
        self.birth_date = birth_date

        # birth_date: "1998-11-20"
        # now = datetime.utcnow()
        # # year, month, day = ["1998". "11", "20"]
        # year, month, day = map(int, birth_date.split("-"))
        # birth_dt = datetime(year=year, month=month, day=day)
        # self.age = (now - birth_dt).days // 365

    def walk(self):
        # self: student1
        # student1.name
        print(f"{self.name} is walking")

    def change_name(self, new_name):
        self.name = new_name

    # ویژگی محاسبه شونده
    @property
    def age(self):
        now = datetime.utcnow() + timedelta(days=3650)
        # year, month, day = ["1998". "11", "20"]
        year, month, day = map(int, self.birth_date.split("-"))
        birth_dt = datetime(year=year, month=month, day=day)
        return (now - birth_dt).days // 365


# mina = Student(name="mina")
# mina.walk()

# asghar = Student(name="asghar")
# asghar.walk()


# instantiate
# create instances
# Student(name="mina")
# Student.__init__(self=student1, name="mina")
# Student.__init__(student1, "mina")
# constructor calls only once
student1 = Student(name="mina", birth_date="1996-04-10")

student2 = Student("mobina", birth_date="2000-04-10")

# access
# attribute
# variable_name.[propertyName]
print(student1.name)
print(student1.asghar)
print(student1.firstname)

# update
# attribute
# new instance
# student1 = Student(name="maryam")
student1.name = "maryam"
print(student1.name)

# behaviour
student1.walk()
# Student.change_name(student1, "gholi")
student1.change_name("gholi")
student1.walk()
# print(student1.get_age())
print(student1.age)
