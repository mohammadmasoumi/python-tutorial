# operator

# arithmetic operator
# +, - , / , *

a = 12
b = 13

print(a + b)
print(a - b)
print(a * b)  # multiplication
print(a / b)  # decision
print(12 / 5)  # decision
print(12 // 5)  # floor
# a = 12
print(12 // a)  # round
print(12 ** 2)  # power
print(13 % 5)
print(12.2 + 13.3)

# int = int + int
print(12 + 12)

# float = int + float
print(12 + 13.3)

# float = float + float
print(13.7 + 12.3)

# TypeError: unsupported operand type(s) for +: 'float' and 'str'
# print(12.2 + 'asds')

# print(12 + 13)
# print(12 + 15)

# assignment operator
a = 12  # assignment
a = a + 2
# a = a + 2
a += 2
a *= 2
a /= 4
a -= 10

a **= 4
a %= 3
a //= 2

b = 10
# b = b + 10
b += 10
print(b)
b -= 10
print(b)

b *= 2
print(b)

# float = int / int
b /= 2
print(b)
# float = int // int
b //= 2

# bitwise operator
print(0 | 0)
print(0 & 0)
print(0 & 1)
print(1 & 1)

print(1 ^ 0)
print(0 ^ 1)
print(1 ^ 1)
print(~0)

# 7 = 111
# 5 = 101
# 111
# 101
# ----
# 111 -> 7

print(7 | 5)

# comparison operator

# output -> boolean
a = 12
b = 12

print(a == b)
print(type(a == b))
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# logical operator
# more than one condition
c = 10
d = 20

print(c == 10 and d == 20)
# True ==> 1. False ==> 0
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

print(c == 10 or d == 20)
# True ==> 1. False ==> 0
# True and True -> True
# True and False -> True
# False and True -> True
# False and False -> False

# not xor in python

print(not (c == 10))
# True ==> 1. False ==> 0
# True -> False
# False -> True

print(2**2**3)