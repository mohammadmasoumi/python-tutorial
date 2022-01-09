"""
mutable Or immutable
1. Changeable (mutable)
2. Ordered => indexing [access to the element]
3. Duplicate
"""

# brackets
my_list1 = [1, 1, 2, 3, 4]

# [positive]0    1      2        3        4
# [negative]-5   -4     -3       -2       -1
my_list2 = [1, False, "Ali", [1, 2, 3], 10.2]

# access element
# TypeError: list indices must be integers or slices, not str
# print(my_list2["Ali"])

# dict
# print(my_list2["Ali"])
print(f"my_list2[2]: {my_list2[2]}")
print(f"my_list2[-3]: {my_list2[-3]}")

