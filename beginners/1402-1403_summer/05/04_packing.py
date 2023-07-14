# 1.
a, b = 12, 13

print(f"a: {a}, b: {b}")

# 2.
# ValueError: not enough values to unpack (expected 3, got 2)
# a, b, c = 12, 14
# print(f"a: {a}, b: {b}, c: {c}")

# 3.
# ValueError: too many values to unpack (expected 2)
# a, b = 12, 13, 14
# print(f"a: {a}, b: {b}")

# 4.
a, b, *c = 12, 13, 14, 15
print(f"a: {a}, b: {b}, c: {c}")

a, *b, c = 12, 13, 14, 15
print(f"a: {a}, b: {b}, c: {c}")

*a, b, c = 12, 13, 14, 15
print(f"a: {a}, b: {b}, c: {c}")

# 5,
# *a, *b, c = 12, 13, 14, 15
# print(f"a: {a}, b: {b}, c: {c}")

# 6.
*a, b, c = 12, 13
print(f"a: {a}, b: {b}, c: {c}")

a, *b, c = 12, 13
print(f"a: {a}, b: {b}, c: {c}")

a, b, *c = 12, 13
print(f"a: {a}, b: {b}, c: {c}")

# application
# 1. for - enumerate
# 2. *args
