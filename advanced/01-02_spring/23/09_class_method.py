from datetime import datetime

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def init_from_birthday(cls, name, birthday):
        # Person(name, age=da)
        return cls(name, datetime.utcnow().year - int(birthday))


# factory method
person1 = Person("asghar", 22)
person2 = Person.init_from_birthday("akbar", "1998")