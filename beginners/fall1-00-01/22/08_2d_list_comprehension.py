# comprehension

"""
n = 11
n = 10
# 11 % 2 = 1
# 10 % 2 = 0

# if 1: bool(1) => True
# if 0: bool(0) => False
if n % 2:
    print("Odd")
else:
    print("Even")
"""

two_d_array = [[1, 2, 3], [4, 5, 6]]

# items: [1, 2, 3], item: 1, 2, 3
# items: [4, 5, 6], item: 4, 5, 6
# flat 2d array
my_list = [item for items in two_d_array for item in items]  # [1, 2, 3, 4 ,5 ,6]
my_list2 = [item for items in two_d_array for item in items if item % 2]  # [1, 3 ,5]
my_list3 = [item * 2 if item % 2 else item // 2 for items in two_d_array for item in items]  # [2, 1, 6, 2, 10, 3]

print(my_list)
print(my_list2)
print(my_list3)

# my_list22 = []
# for items in two_d_array:
#     for item in items:
#         my_list22.append(item)
#
three_d_array = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print(three_d_array[0][1][1])
