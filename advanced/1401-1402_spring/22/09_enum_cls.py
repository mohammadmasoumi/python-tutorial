from enum import Enum


Animal = Enum("Animal", "ANT BEE CAT DOG") # auto()

print(Animal.ANT.name)
print(Animal.ANT.value)

print(Animal.CAT.name)
print(Animal.CAT.value)