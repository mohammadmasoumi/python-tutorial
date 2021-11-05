from datetime import datetime, timedelta


class Student:

    def __init__(self, name, birth_date):
        self._name = name
        self._birth_date = birth_date

    # a behavior which we make it property
    @property
    def age(self):
        print(self._birth_date)
        return (datetime.utcnow() - self._birth_date).days // 365

    # def age(self):
    #     print(self._birth_date)
    #     return (datetime.utcnow() - self._birth_date).days // 365


noah = Student("Noah", datetime.utcnow() - timedelta(days=300000))
print(f"{noah._name} is {noah.age} years old.")

# noah.age
# noah.age()
