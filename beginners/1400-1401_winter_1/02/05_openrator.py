# arithmetic operators

# int
a = 12 
b = 13

print("12 + 13 =", a + b)
print("12 - 13 =", a - b)
print("12 / 13 =", a / b) # floating point division
print("90 / 10 =", 90 / 10) # result: float
print("90 // 10 =", 90 // 10) # result: int
print("12 * 13 =", a * b) # multiplication
print("12 ** 13 =", a ** b) # pow

# str
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(12 + "ali")
print("12" + "ali") # concantenation
print("Hello" + "World")
print("Ali" + "Reza")
print("Ali " + "Reza")
print("Ali" + " Reza")
print("Ali" "Reza" "welcome" "to" "the" "course")
print("Ali", "Reza", "welcome", "to", "the", "course")
print("Ali", "Reza", "welcome", "to", "the", "course", sep="*")

print(True + 12)
print(False + 12)

# print("Ali" + True)
print("Ali" + "True")
print('Ali' + "True")

# NameError: name 'Ali' is not defined
# print(Ali + True)
# print(Ali + "True")

