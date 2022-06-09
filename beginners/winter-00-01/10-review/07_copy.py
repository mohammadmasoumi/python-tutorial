# 1. shallow copy
# 2. deep copy

# without copy
my_list1 = [1, 2, 3, 4]
my_list2 = my_list1

my_list1.append(5)

print(my_list1)
print(my_list2)
print("----------------------")

# shallow copy
my_list1 = [1, 2, 3, 4]
my_list2 = my_list1.copy()

my_list1.append(5)

print(my_list1)
print(my_list2)
print("----------------------")

# deep copy
from copy import deepcopy

my_list1 = [[1, 2], 3, 4]
my_list2 = deepcopy(my_list1)
# my_list2 = my_list1.copy()

my_list1[0].append(5)

print(my_list1)
print(my_list2)

