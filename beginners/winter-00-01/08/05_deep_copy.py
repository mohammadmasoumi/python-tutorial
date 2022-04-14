# shallow copy
from copy import deepcopy

# shallow copy
my_list1 = [[1, 2], 10, 11]
my_list2 = my_list1.copy()
my_list1[0].append(5)
my_list2[0].append(6)

print(f"my_list1: {my_list1}")
print(f"my_list2: {my_list2}")
print("-------------------------")

# solve
my_list3 = [[1, 2], 10, 11]
my_list4 = deepcopy(my_list3)
my_list3[0].append(5)
my_list4[0].append(6)

print(f"my_list3: {my_list3}")
print(f"my_list4: {my_list4}")





