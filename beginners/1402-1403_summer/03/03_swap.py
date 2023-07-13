# 1. temp varialbe
a = 12
b = 13

c = a
a = b
b = c
print(a, b)

# 2. arithmetic operator
a = 12
b = 13

a = a + b  # a: 25, b: 13
b = a - b  # a: 25, b: 12
a = a - b  # a: 13, b: 12

print(a, b)

# 3. python
# matching
# packing
a = 12
b = 13

a, b = b, a

print(a, b)
