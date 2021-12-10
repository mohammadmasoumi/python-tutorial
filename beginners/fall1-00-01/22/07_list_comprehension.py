# list comprehension

my_list = [1, 2, 3, 4]

# [ item for item in iterable]
my_list2 = [item * 2 for item in my_list]
# item % 2 [0, 1]
# if 0:
# if 1:
my_list3 = [item * 2 for item in my_list if item % 2]  # [1, 2, 3, 4] => [1, 3], odd
my_list4 = [item * 2 for item in my_list if item % 2 == 0]  # [1, 2, 3, 4] => [2, 4], even
my_list5 = [item // 2 if item % 2 == 0 else item * 2 for item in my_list]  # [2, 1, 6, 2]

condition = False
# true_value if condition else false_value
a = 12 if condition else 13

# a = 12 if condition is True
# a = 13 if condition is False

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
print(my_list5)
