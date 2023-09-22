from datetime import datetime
# Pascal casing
# StudentName


class Student:
    # only run once
    def __init__(self, name, birthdate):
        self.name = name
        # self.age = age
        self.birthdate = birthdate

    # decorator
    @property
    def age(self):  # cast behaviour -> property
        return (datetime.utcnow() -
                datetime.strptime(self.birthdate, "%Y-%m-%d")).days // 365


# variable name - snake casing
# ali = Student(name="ali", age=20)
# fatemeh = Student(name="fatemeh", age=19)
ali = Student(name="ali", birthdate="1996-03-04")
fatemeh = Student(name="fatemeh", birthdate="2003-02-20")

students = [ali, fatemeh]

# age: calculated property
# print(ali.name, ali.age())  # age: property -> age:behaviour
# print(fatemeh.name, fatemeh.age())

print(ali.name, ali.age)  # age: property -> age:behaviour
print(fatemeh.name, fatemeh.age)
