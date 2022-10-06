# cast - change the type of a variable

# built-in function
# print
# type

# = assignment
# variable = value
# assign the value into variable

# int
a1 = int(12) # a1: 12 | int -> int
a2 = int(12.5) # a2: 12 | float -> int
# ValueError: invalid literal for int() with base 10: 'Ali'
# a3 = int("Ali") str -> int
a4 = int("12") # str -> int
a5 = int(True) # bool -> int | 1
a6 = int(False) # bool -> int | 0
# a7 = int(" ") # Error
# a8 = int("") # Error

print("a1:", a1, type(a1))
print("a2:", a2, type(a2))
# print("a3", a3)
print("a4:", a4, type(a4))
print("a5:", a5, type(a5))
print("a6:", a6, type(a6))

print("--------------------")

# float
b1 = float(12) # 12.0
b2 = float(12.5) # 12.5
# b3 = float("Ali") # Error
b4 = float("12") # 12.0 
b5 = float("12.5") # 12.5
b6 = float(True) # 1.0
b7 = float(False) # 0.0
b8 = float("12 ") #  remove extra spaces
b9 = float("12       ") # remove extra spaces
# b10 = float("12       *") # Error
# b11 = float("12       12")

print("b1:", b1 ,type(b1))
print("b2:", b2 ,type(b2))
# print("b3", b3 ,type(b3))
print("b4:", b4 ,type(b4))
print("b5:", b5 ,type(b5))
print("b6:", b6 ,type(b6))
print("b7:", b7 ,type(b7))
print("b8:", b8 ,type(b8))
print("b9:", b9 ,type(b9))
# print("b10:", b10 ,type(b10))
# print("b11:", b11 ,type(b11))

print("--------------------")

# str
c1 = str(12) # "12"
c2 = str(12.5) # "12.5"
c3 = str("Ali") # "Ali"
c4 = str("12") # "12"
c5 = str(True) # "True"
c6 = str(False) # "False"

print("c1:", c1, type(c1))
print("c2:", c2, type(c2))
print("c3:", c3, type(c3))
print("c4:", c4, type(c4))
print("c5:", c5, type(c5))
print("c6:", c6, type(c6))

print("--------------------")

# bool
# Flase values: 0, 0.0, "" 

d1 = bool(12) # True
d2 = bool(0) # False
d3 = bool(-12) # True
d4 = bool(10000000000000) # True
d5 = bool(12.5) # True
d6 = bool(0.0) # False
d7 = bool(-12.5) # True
d8 = bool("Ali") # True
d9 = bool("") # Flase
d10 = bool("0") # True
d11 = bool(" ") # True
d12 = bool(False) # Flase
d13 = bool(True) # True

print("d1:", d1, type(d1))
print("d2:", d2, type(d2))
print("d3:", d3, type(d3))
print("d4:", d4, type(d4))
print("d5:", d5, type(d5))
print("d6:", d6, type(d6))
print("d7:", d7, type(d7))
print("d8:", d8, type(d8))
print("d9:", d9, type(d9))
print("d10:", d10, type(d10))
print("d11:", d11, type(d11))
print("d12:", d12, type(d12))
print("d13:", d13, type(d13))