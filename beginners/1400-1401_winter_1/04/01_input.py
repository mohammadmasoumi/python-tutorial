# built-in function
# input 

# Immutable
# int
# str
# bool
# float
# tuple

# Mutable
# list, set, dict

# input always get you str
number1 = input()
number2 = input()

print(type(number1)) # "12"
print(type(number2)) # "13"

# concatenation
# "12" + "13" => "1213"
# c = number1 + number2
# print(c)
print(number1 + number2)

# change the type on the fly
print(int(number1) + int(number2)) # we change the type just here!

print(type(number1)) # "12"
print(type(number2)) # "13"

# change the type persistant 
number1 = int(number1)
number2 = int(number2)

print(type(number1)) # 12
print(type(number2)) # 13

print(number1 + number2)
