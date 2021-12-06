my_list = [1, 2, 3, 4]

# a = my_list[0]
# b = my_list[1]
# c = my_list[2]
# d = my_list[3]

# a, b, c, d = [1, 2, 3, 4]
# a, b, c, d = 1, 2, 3, 4

# a <=> 1
# b <=> 2
# c <=> 3
# d <=> 4
a, b, c, d = my_list

# alternative
# a1, b1 = 12 ,13
# a1 = 12
# b1 = 13

# -----------------------------------------------------
# [1, 2, 3, 4]
# ValueError: too many values to unpack (expected 3)
# a1 <=> 1
# b1 <=> 2
# c1 <=> 3
# ?? <=> 4
# a1, b1, c1 = my_list

# -----------------------------------------------------
# [1, 2, 3, 4]
# a2 <=> 1
# b2 <=> 2
# c2 <=> 3
# d2 <=> 4
# e2 <=> ??
# ValueError: not enough values to unpack (expected 5, got 4)
# a1, b1, c1, d1, e1 = my_list

# -------------------------------------------------------
# [1, 2, 3, 4]
*a4, b4, c4 = my_list
a5, *b5, c5 = my_list
a6, b6, *c6 = my_list

print(*a4, b4, c4)
print(a4, *b4, c4)
print(a4, b4, *c4)

# -------------------------------------------------------
my_list2 = [1, 2, 3, 4, 5]
# SyntaxError: multiple starred expressions in assignment
# a7, *b7, *c7 = my_list2
