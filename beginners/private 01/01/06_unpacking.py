# unpacking
my_list = [1, 2, 3]

a, b, c = my_list
a1, b1, c1 = [1, 2, 3]
a2, b2, c2 = 1, 2, 3

print(f"a: {a}, b: {b} ,c: {c}")
print(f"a1: {a1}, b1: {b1} ,c1: {c1}")
print(f"a2: {a2}, b2: {b2} ,c2: {c2}")

# [], [] = O O O
# ValueError: too many values to unpack (expected 2)
# a3, b3 = [1, 2, 3]
# print(f"a3: {a3}, b3: {b3}")

# [], [], [] = O O
# ValueError: not enough values to unpack (expected 3, got 2)
# a4, b4, c4 = [1, 2]
# print(f"a4: {a4}, b4: {b4}, c4: {c4}")

# Packing
# [] [] [] = O O O O
*a5, b5, c5 = [1, 2, 3, 4]
print(f"a5: {a5}, b5: {b5}, c5: {c5}")

a6, *b6, c6 = [1, 2, 3, 4]
print(f"a6: {a6}, b6: {b6}, c6: {c6}")

a7, b7, *c7 = [1, 2, 3, 4]
print(f"a7: {a7}, b7: {b7}, c7: {c7}")

# SyntaxError: two starred expressions in assignment
# a8, *b8, *c8 = [1, 2, 3, 4, 5]
# print(f"a8: {a8}, b8: {b8}, c8: {c8}")
