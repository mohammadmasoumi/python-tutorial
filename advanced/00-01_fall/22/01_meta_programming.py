"""
meta programming

everything is object in python.
"""


class Person:
    pass


person = Person()

print(person.__class__)

print(type(person))
print(type(Person))
print(type(type))

print(type(person) is person.__class__)
