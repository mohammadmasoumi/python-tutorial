# list comprehension

my_list = [1, 2, 3, 4]


def is_no_even(item):
    return item % 2 == 0


# TypeError: int() argument must be a string, a bytes-like object or a number, not 'filter'
# print(int(filter(is_no_even, my_list)))

print(filter(is_no_even, my_list))
print(list(filter(is_no_even, my_list)))

# another way of filtering
# my_list = [1, 2, 3, 4]
print([item * 2 for item in my_list])
print([item * 2 for item in my_list if item % 2 == 0])
# [[true_statement if condition else false_statement for item in my_list]]
print([item // 2 if item % 2 == 0 else item * 2 for item in my_list])

my_list2 = []
for item in my_list:
    if item % 2 == 0:
        my_list2.append(item * 2)

# -----------------------------------------
my_list3 = [range(3), range(3)]
print([item * 2 for items in my_list3 for item in items if item % 2 == 0])
print([item // 2 if item % 2 == 0 else item * 2  for items in my_list3 for item in items])

# ml = [1, 2, 3, 4]
#
# for i in ml:
#     for j in range(i):
#         print(f"i: {i}, j: {j}")

# string as list
# ml2 = ["apple", "peach"]
# for item in ml2:
#     for chr in item:
#         print(chr)
#     print("")
