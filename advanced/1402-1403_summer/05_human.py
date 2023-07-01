from datetime import datetime, timedelta

# Problem
# class Human:

#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age


# # year: 1402
# h1 = Human(name="yadollah", gender="male", age=70)
# h2 = Human(name="mitra", gender="female", age=10)

# # 1403
# print(h1.age)
# print(h2.age)


# # Solution - Problem
# class Human:

# Constructor only call once
#     def __init__(self, name, gender, birth_date):
#         self.name = name
#         self.gender = gender

#         # string, format -> new datetime parsed from a string (like time.strptime()).
#         # string -> datetime
#         birth_dt = datetime.strptime(birth_date, "%Y-%m-%d")
#         now = datetime.utcnow()
#         self.age = (now - birth_dt).days // 365


# # year: 2023
# h1 = Human(name="mohammad", gender="male", birth_date="1996-03-04") # call constructor
# h2 = Human(name="imani", gender="male", birth_date="2008-10-30")

# # 2024
# print(h1.age)
# print(h2.age)


# # Solution - Problem
# class Human:

#     def __init__(self, name, gender, birth_date):
#         self.name = name
#         self.gender = gender
#         self.birth_date = birth_date

#     # age: property
#     # propery -> behaviour
#     def age(self):
#         birth_dt = datetime.strptime(self.birth_date, "%Y-%m-%d")
#         now = datetime.utcnow()
#         return (now - birth_dt).days // 365


# # year: 2023
# h1 = Human(name="mohammad", gender="male", birth_date="1996-03-04")
# h2 = Human(name="imani", gender="male", birth_date="2008-10-30")

# # 2024
# print(h1.age())
# print(h2.age())

# Solution
class Human:

    def __init__(self, name, gender, birth_date):
        self.name = name
        self.gender = gender
        self.birth_date = birth_date

    # age: property
    # propery -> behaviour
    # calculable
    # ویژگی های محاسبه شونده
    @property
    def age(self):
        birth_dt = datetime.strptime(self.birth_date, "%Y-%m-%d")
        now = datetime.utcnow()
        return (now - birth_dt).days // 365


# year: 2023
h1 = Human(name="mohammad", gender="male", birth_date="1996-03-04")
h2 = Human(name="imani", gender="male", birth_date="2008-10-30")

# 2024
print(h1.age)
print(h2.age)
