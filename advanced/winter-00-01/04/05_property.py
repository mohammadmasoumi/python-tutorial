from datetime import datetime

# attribute -> constructor
# behaviour -> function, method

class Student:
    # constructor

    # national_id, personality_type, father_name, pet_name, height
    def __init__(self, name, birthday):
        # instanc: self
        #    attr   value
        # attribute
        # 2020-10-11
        self.name = name
        self.birthday = birthday

    # attribute - function
    @property
    def age(self):
        utcnow = datetime.utcnow()
        year, month, day = map(int, self.birthday.split("-"))
        birth_date = datetime(year=year, month=month, day=day)
        return (utcnow - birth_date).days // 365

    # behaviour
    def move(self):
        print(f"[{self.name}]: I am moving")

std = Student("ali", "1998-10-2")
std.move()
print(std.name)
print(std.birthday)
print(std.age)
