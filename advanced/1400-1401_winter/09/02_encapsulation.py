# encapsulation

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name


person1 = Person("aliakbar", 17)
person2 = Person("ali", 21)

# name: property
print(person1.name)
print(person1.age)

# how to change person1's name?
person1.name = "aliasghar"
print(person1.name)

# define a new function - encasulated [tick]
person1.change_name("aliakbar")
print(person1.name)
