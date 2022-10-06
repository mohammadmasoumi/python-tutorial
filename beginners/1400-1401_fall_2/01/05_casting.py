# casting

# built-in function
# type
# print
# int

# khuruji = int(vorodi)

# int
a1 = 12
a2 = int(12)  # int -> int
a3 = int(True)  # bool -> int
a4 = int(False)  # bool -> int
a5 = int(12.9)  # float -> int - drop floating point part
a6 = int(12.1)  # float -> int - drop floating point part

# ValueError: invalid literal for int() with base 10: 'a'
# a7 = int("a")  # str -> int - raise exception
# a8 = int("56a")  # str -> int - raise exception
a8 = int("56")  # str -> int

print(a1, type(a1))
print(a2, type(a2))
print(a3, type(a3))
print(a4, type(a4))
print(a5, type(a5))
print(a6, type(a6))
# print(a7, type(a7))
print(a8, type(a8))

print("--------------------------------------")
# float

b1 = float(12.2)  # float -> float
b2 = float(12)  # int -> float
b3 = float(True)  # bool -> float
b4 = float(False)  # bool -> float
b5 = float("1")  # str -> float
b6 = float("1.9")  # str -> float

# ValueError: could not convert string to float: 'a'
# b7 = float("a")  # str -> float

print(b1, type(b1))
print(b2, type(b2))
print(b3, type(b3))
print(b4, type(b4))
print(b5, type(b5))
print(b6, type(b6))
# print(b7, type(b7))

print("--------------------------------------")

# bool - True, False

# false values
# int: 0
# float : 0.0
# str: "", ''

c1 = bool(True)  # bool -> bool
c2 = bool(False)  # bool -> bool
c3 = bool(1)  # int -> bool - True
c4 = bool(12)  # int -> bool - True
c5 = bool(0)  # int -> bool - False - false values
c6 = bool(-10)  # int -> bool
c7 = bool(0.0)  # float -> bool
c8 = bool(0.1)  # float -> bool
c9 = bool("ali")  # str -> bool
c10 = bool("12")  # str -> bool
c11 = bool(" ")  # str -> bool
c12 = bool("0")  # str -> bool
c13 = bool("")  # str -> bool
c14 = bool('')  # str -> bool

print(c1, type(c1))
print(c2, type(c2))
print(c3, type(c3))
print(c4, type(c4))
print(c5, type(c5))
print(c6, type(c6))
print(c7, type(c7))
print(c8, type(c8))
print(c9, type(c9))
print(c10, type(c10))
print(c11, type(c11))
print(c12, type(c12))
print(c13, type(c13))
print(c14, type(c14))

print("--------------------------------------")

# str

d1 = str("ali")  # str -> str
d2 = str(12)  # int -> str
d3 = str(12.2)  # float -> str
d4 = str(True)  # bool -> str
d41 = "True"
d5 = str(False)  # bool -> str
d51 = "False"
d52 = 'False'

print(d1, type(d1))
print(d2, type(d2))
print(d3, type(d3))
print(d4, type(d4))
print(d5, type(d5))
