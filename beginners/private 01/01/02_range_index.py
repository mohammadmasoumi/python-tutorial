"""
mutable Or immutable
1. Changeable (mutable)
2. Ordered => indexing [access to the element]
3. Duplicate
"""

# [pos]     0    1      2        3        4
# [neg]    -5   -4     -3       -2       -1
my_list = [1, False, "Ali", [1, 2, 3], 10.2]

# negative step
#                  <-----------------------------------------------------------
#  # [pos]     0    1      2        3        4                               10
#           start end(not included) step
print(my_list[10: 1: -1])  # first element 10.2

#                  <-----------------------------------------------------------
# [pos]  -6 [-4] -3 [-2] -1 [0]  1  [2] 3 [4] 5 [6] 7 [8] 9 [10]
print(my_list[10: -6: -2])

# [pos]  -6 -4 -3 -2 -1 0  1  2 3 [4]
print(my_list[10: -6: -20])

print("--------------------------------------------------")
# negative index
#               not included
print(my_list[-4: -1])
print(my_list[-10: -1])
# -10 [no items]        0 1 2 3 4
print(my_list[-10: 0])  # []

#               2  3  4
#              -3 -2 -1
#              -3     4
print(my_list[-3: 4])

print("--------------------------------------------------")
# index out of range
# IndexError: list index out of range
# [0, ... , 4]
# print(my_list[10])
print(my_list[0])
print(my_list[4])

print("--------------------------------------------------")
# range indexes
#             [start: end(not included): step]
#             start:1 , end: 2, step: 1
print(my_list[1:2])  # [False]
print(my_list[1:3])  # [False, "Ali"]
print(my_list[1:10])  # do not raise exception
print(my_list[2:2])  # []
print(my_list[2:3])  # ["Ali"]
print(my_list[10:3])  # []
