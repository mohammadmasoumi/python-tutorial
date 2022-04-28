# unpacking

# unpacking
a, b = [1, 2]

# define multiple variables in one line
a1, b1 = 1, 2

# a1 = 1
# b1 = 2
# a1, b1 = 1 ,2
# a, b = 1, 2
# print(f"a: {a}, b: {b}")

# ?
# ValueError: not enough values to unpack (expected 3, got 2)
# a, b, c = [1, 2]
# print(f"a: {a}, b: {b}, c: {c}")

# ?
# ValueError: too many values to unpack (expected 2)
# a, b = [1, 2, 3]
# print(f"a: {a}, b: {b}")


# packing with * 
# [1, 2]
*a, b, c = [1, 2, 3, 4]
print(f"a: {a}, b: {b}, c: {c}")

a, *b, c = [1, 2, 3, 4]
print(f"a: {a}, b: {b}, c: {c}")

a, b, *c = [1, 2, 3, 4]
print(f"a: {a}, b: {b}, c: {c}")


