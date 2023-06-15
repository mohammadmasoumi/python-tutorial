from datetime import datetime, timedelta


class Student:
    # Constructor
    # Create instance
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # only calls when you are creating the instance
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.scores = [10, 10, 10]

    # you have to calculate
    @property
    def age(self):  # property -> behaviour ?
        # string -> datetime
        birth_dt = datetime.strptime(self.birth_date, "%m-%d-%Y")
        # now = datetime.now()
        now = datetime.now() - timedelta(days=365)
        return (now - birth_dt).days // 365

    @property
    def grade(self):
        return sum(self.scores) // len(self.scores)

    # age: property vs behaviour


# mina = Student("mina", 34)
# asghar = Student("asghar", 2)
mina = Student("mina", "12-12-1988")
# print(mina.age())
print(mina.age)
print(mina.grade)
mina.scores.append(20)
print(mina.grade)
# 1 year later
# print(mina.age())
