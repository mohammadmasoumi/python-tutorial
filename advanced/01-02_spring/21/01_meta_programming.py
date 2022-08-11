"""
meta programming
Everything is object in python.
"""

class Person:
    pass

person = Person()

print(person.__class__) # Person

print(type(person)) # Person
print(type(Person)) # type 
print(type(type)) # type

#     Person                Person
print(type(person) is person.__class__)