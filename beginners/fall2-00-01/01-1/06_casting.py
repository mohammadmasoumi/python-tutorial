# casting

# type -> type

"""
'1' str -> 1 int

built-in function
int
str
float
bool
"""

# int_datatype = int(variable or value)
# datatype1 -> datatype2

# False values:
# int: [0], float: [0.0], str: ["", '']

# int
a = 12

a1 = int(a)  # int -> int
a2 = float(a)  # int -> float - 12.0
a3 = str(a)  # int -> str - "12" or '12' - "455"
a4 = bool(a)  # int -> bool - [True, False]
a5 = bool(0)  # int -> bool - [True, False]
a6 = bool(-1)  # int -> bool - [True, False]
a7 = bool(10000000000000)  # int -> bool - [True, False]

print(a1, type(a1))
print(a2, type(a2))
print(a3, type(a3))
print(a4, type(a4))
print(a5, type(a5))
print(a6, type(a6))
print(a7, type(a7))

print("-------------------------------------------")
# float

b = 12.2
b1 = float(b)  # float -> float
b2 = int(b)  # float -> int - 12
b3 = int(12.9)  # float -> int - 12 0 drop float point
b4 = str(b)  # float -> str - "12.2" or '12.2'
b5 = bool(b)  # float -> bool - True
b6 = bool(0.0)  # float -> bool - False

print(b1, type(b1))
print(b2, type(b2))
print(b3, type(b3))
print(b4, type(b4))
print(b5, type(b5))
print(b6, type(b6))

print("-------------------------------------------")
# str

c = "Hello world!"
d = "12"
e = "12a"
f = "0"
g = ""
h = ''
k = ' '  # str -> bool True

c1 = str(c)  # str -> str
d1 = str(d)  # str -> str

# ------------------
# ValueError: invalid literal for int() with base 10: 'Hello world!'
# c2 = int(c)  # str -> Raise exception
d2 = int(d)  # str -> int
# ValueError: invalid literal for int() with base 10: '12a'
# e2 = int(e)  # str -> int

# ------------------
# ValueError: could not convert string to float: 'Hello world!'
# "C:\Users\MFT\PycharmProjects\beginners\01-1\06_casting.py"
# c3 = float(c)  # str -> float

d3 = float(d)  # str -> float
# ------------------

c4 = bool(c)  # str -> bool
d4 = bool(d)  # str -> bool
e4 = bool(e)  # str -> bool
f4 = bool(f)  # str -> bool
g4 = bool(g)  # str -> bool
h4 = bool(h)  # str -> bool
k4 = bool(k)  # str -> bool

# ------------------
print(c1, type(c1))
print(d1, type(d1))

# ------------------
# print(c2, type(c2))
print(d2, type(d2))
# print(e2, type(e2))

# -------------------
# print(c3, type(c3))
print(d3, type(d3))

# -------------------
print(c4, type(c4))
print(d4, type(d4))
print(e4, type(e4))
print(f4, type(f4))
print(g4, type(g4))
print(h4, type(h4))
print(k4, type(k4))

print("-------------------------------------------")
# bool

n = True
m = False

n1 = int(n)  # bool -> int
m1 = int(m)  # bool -> int

n2 = float(n)  # bool -> float
m2 = float(m)  # bool -> float

n3 = str(n)  # bool -> str - "True" or 'True'
m3 = str(m)  # bool -> str - 'False' or "False"

n4 = bool(n)  # bool -> bool
m4 = bool(m)  # bool -> bool

print(n1, type(n1))
print(m1, type(m1))

print(n2, type(n2))
print(m2, type(m2))

print(n3, type(n3))
print(m3, type(m3))

print(n4, type(n4))
print(m4, type(m4))
