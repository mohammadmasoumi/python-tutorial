from datetime import datetime

# a = input()
# a = int(a)
# a = int(input())
# list(map(lambda x: x*2, [1, 2, 3]))

class Student:

    # constructor
    def __init__(self, name, birthday):
        # self
        # std1.name
        # std1.birthday
        
        # private
        self.__name = name
        self.birthday = birthday
        # private
        self.__scores = []
        self.school = "Shahid Sattari"

    @property
    def age(self):
        year, month, day = map(int, self.birthday.split("-"))
        return (datetime.utcnow() - datetime(year=year, month=month, day=day)).days // 365

    @property
    def avg(self):
        return sum(self.__scores) / len(self.__scores) if self.__scores else 0

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self, new_value):
        pass

    @scores.deleter
    def scores(self):
        pass

    def add_score(self, score):
        if self.__name == "zahra" and score < 20:
            self.__scores.append(20)
        else:
            self.__scores.append(score)

    def remove_score(self, score):
        self.__scores.remove(score)

    # get
    @property
    def name(self):
        return self.__name

    # set
    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str):
            self.__name = new_value
    
    # del
    @name.deleter
    def name(self):
        pass


# Student(std1, "asghar", "1998-02-02")
std1 = Student("asghar", "1998-02-02")
std2 = Student("akbar", "1996-02-02")
std3 = Student("zahra", "1996-02-02")

# get
# print(std1.__name)
print(std1.name)
# print(std1.birthday)
print(std1.scores)
print(std1.school)

std1.name = 12
print(std1.name)

std1.name = "Mina"
print(std1.name)

# std1.scores = [12, 20 , 2]
# print(std1.scores)

std3.add_score(2)
print(std3.scores)
std3.remove_score(20)
print(std3.scores)


# print(std3.get_age())
# print(std2.get_age())
# print(std1.get_age())

print(std3.age)
print(std2.age)
print(std1.age)
print(std3.avg)


# print(std1.name()) => print(std1.name)


# set
# std1.name = "aliasghar"
# print(std1.name)

# del
# del std1.name
# print(std1.name)
