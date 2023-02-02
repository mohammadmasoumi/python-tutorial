# arithmetic operators
import math

"""
built-in function
    - print
    - pow
"""

a = 12
b = 13

c = a + b
c = a - b
d = a * b

# float div
e = 24 / 2 # e: 12.0 float
# true div
f = 22 // 5 # 4.4 => 4 int

# power
g = 2 ** 10
g = pow(2, 10)# built-in function

h = math.sqrt(16)
print(h)

j = 20 % 3 # reminder - mod
print(j)


# -----------------------
# concatenation

print("ali" + "reza") #  alireza
print("ali" + " reza") # ali reza
print("ali " + "reza") # ali reza

a = "ali"
b = "reza"
print(a + b)
print(a+b)
print(a +                   b)
print("a" +                   "b")

# NameError: name 'x' is not defined
# print("a" +                  x)


