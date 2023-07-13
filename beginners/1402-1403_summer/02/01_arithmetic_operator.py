# Arithmeric operator
import math

a = 120
b = 13

c1 = a + b
c2 = a * b
c3 = a ** b  # a ^b
c4 = a / b  # floar div - عدد اعشاری
c5 = a // b  # true div - عدد صحیح

c6 = a % b
c7 = a ** (0.5)
c8 = math.sqrt(a)  # جذر
c9 = math.pow(a, 2)  # a ** 2

print(math.floor(3.14))
print(math.ceil(3.14))

# x < 0 -> -x
# x > 0 -> x
print(abs(-12))  # absulute value
print(abs(12))

print(c5, c6, c7, c8, c9)

# --------------
# True => 1
# False => 0
print(1.2 * True)  # 1.2
print(12 * False)  # 0

print(1.2 + True)  # 2.2
print(12 + False)  # 12

print("----------")

print(12 + 12.2)  # 24.2
# int + float => float
print(12 + 12.0)  # 24.0

# float + flaot => flaot
print(12.5 + 12.5)  # 25.0

# int + int = int
print(12 + 12)

print("----------")
# aliali
print("ali" * 2)  # 2ali, aliali, yaali, ali2, aallii,
print("ali" * 10)

# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print("ali" / 2 )

# TypeError: can't multiply sequence by non-int of type 'float'
# print("ali" * 2.2)

# TypeError: can't multiply sequence by non-int of type 'str'
# print("ali" * "agha") #

# TypeError: can only concatenate str (not "int") to str
# print("ali" + 2)  # ali2, ali, error
# TypeError: can only concatenate str (not "float") to str
# print("ali" + 2.2)  # ali2, ali, error

# concatenation
# "ali" + "agha" -> "aliagha"

print("ali" * True)  # "ali" * 1 => "ali"
print("ali" * False)  # ""
print("")
# TypeError: can't multiply sequence by non-int of type 'float'
# print("ali" * 0.5) # exception

# print("ali" * 5 / 5)
# "alialialialialiali" / 5
# TypeError: can't multiply sequence by non-int of type 'float'
# print("ali" * 1.0)
# print("ali" * (5 / 5))
print("ali" * (5 // 5))  # "ali" * 1

# power توان
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# print("ali"**2)

# print("ali" - 12)
# print("ali" - 12.02)

# TypeError: unsupported operand type(s) for -: 'str' and 'int'
# print("13" - 2)
