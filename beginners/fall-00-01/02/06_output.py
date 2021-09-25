# version 3.9 - 4.1

a = 10
name = "Mohammad"
phone_number = 123456789
weight = 82.9
# f-string 3.6 >

print("Hello world")

# {} braces
# {} curly braces
print(f"Hello {name}")  # str
print(f"My number is: {phone_number}")  # int
print(f"My weight is: {weight}")  # float

# -----------------------------------------------
# for python version 3.6 < you must use format
# format 3.2 , ... 3.9
print("Hello {}".format(name))
x1 = 10
x2 = 20
print("Hello {} and {}".format(x1, x2))

# IndexError: Replacement index 2 out of range for positional args tuple
# print("Hello {} and {} and {}".format(x1, x2))

print("Hello {value1} and {value2}".format(value2=x1, value1=x2))
