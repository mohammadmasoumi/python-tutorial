# swap

a = 12
b = 13

c = a
a = b
b = c

print(a, b)
#------------------------------------
a = 12
b = 13

a = a + b
b = a - b
a = a - b

print(a, b)
#------------------------------------

a = 12
b = 13

a, b = b, a

print(a, b)
#------------------------------------