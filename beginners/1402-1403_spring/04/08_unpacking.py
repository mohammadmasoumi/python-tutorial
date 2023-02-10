# unpacking and packing

# mutable
# [1, 2] list

# immutable
# (1, 2) tuple

a = 12
b = 13

a, b = b, a

print(a, b)

# ValueError: too many values to unpack (expected 2)
# a, b = 12, 13, 14

# ValueError: not enough values to unpack (expected 3, got 2)
# a, b, c = 12, 13

a, b = (12, 13), 14
print(a, b)

*a, b = 12, 13, 14
print(a, b)

*a, b = 12, 13, 14, 15, 16, 17
print(a, b)

a, *b = 12, 13, 14, 15, 16, 17
print(a, b)

# SYNTAX error
# *a, *b = 12, 13, 14, 15, 16, 17
# print(a, b)

a, *b, c = 12, 13, 14, 15, 16, 17
print(a, b, c)

*a, b, c = 12, 13, 14, 15, 16, 17
print(a, b, c)

a, b, *c = 12, 13, 14, 15, 16, 17
print(a, b, c)