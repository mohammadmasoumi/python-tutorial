# arithmetic list

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

# merge two list
#           [1, 2, 3, 4, 5, 6]
my_list3 = my_list1 + my_list2

# TypeError: unsupported operand type(s) for -: 'list' and 'list'
# my_list3 = my_list1 - my_list2

print(my_list3)
print("-----------")

my_list4 = my_list1 * 2
print(my_list4)

# error
# [4, 5, 6]
# [1, 2, 3, 1, 2, 3]
# [[1, 2, 3], [1, 2, 3]]

# TypeError: unsupported operand type(s) for /: 'list' and 'int'
# my_list5 = my_list1 / 2
# print(my_list5)

# [[1, 2, 3, 1, 2, 3]]
my_list6 = [my_list1 * 2]
print(my_list6)

#
# print(my_list7[0] is my_list7[1]) False
my_list7 = [[1, 2, 3] for _ in range(10)]
# print(my_list7[0] is my_list7[1]) True
my_list7 = [my_list1 for _ in range(10)]
print(my_list7)
# [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(my_list7[0] is my_list7[1])

"""
my_list7

| * | * | * |   |   |   |   |   |   |   |

| 1 | 2 | 3 |   |   |   |   |   |   |   |
"""

my_list = [1, 2, 3, 4, 5, 6]
print(id(my_list), id(my_list[::2]))
print(my_list[::2])
del my_list[::2]  # [1, 3, 5]
print(my_list)

print("------------------------")
my_list = [1, 2, 3, 4, 5, 6]
my_list[::2] = [10, 20, 30]
print(my_list)
