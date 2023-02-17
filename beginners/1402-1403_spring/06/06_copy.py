# copy

"""
shallow copy
deep copy
"""
# problem

my_list1 = [1, 2, 3, 4]
my_list2 = my_list1

"""
my_list1 👉 [1,2,3,4] 👈 my_list2
"""

my_list2.append(5)
print(my_list1, my_list2)
print(my_list1 is my_list2)

"""
my_list1 => [1,2,3,4] <= my_list2
my_list2.append(5)
my_list1 => [1,2,3,4,5] <= my_list2
"""

# copy - shallow copy
my_list1 = [1, 2, 3, 4]
my_list2 = my_list1.copy()

my_list2.append(5)
print(my_list1, my_list2)
print(my_list1 is my_list2)

"""
my_list1 => [1,2,3,4]
[1,2,3,4,5] <= my_list2
my_list2.append(5)
"""

# problem
my_list1 = [1, 2, 3, 4, [5, 6]]
my_list2 = my_list1.copy()

my_list2[4].append(7)
print(my_list1, my_list2)
print(my_list1 is my_list2)
print(my_list1[4] is my_list2[4])

"""
my_list1 => [1,2,3,4, 👇]
                    [5, 6]
            [1,2,3,4, 👆] <= my_list2

my_list2[4].append(7)

my_list1 => [1,2,3,4, 👇]
                    [5, 6, 7]
            [1,2,3,4, 👆] <= my_list2
"""

# deep copy
from copy import deepcopy

my_list1 = [1, 2, 3, 4, [5, 6]]
my_list2 = deepcopy(my_list1)

my_list2[4].append(7)
print(my_list1, my_list2)
print(my_list1 is my_list2)
print(my_list1[4] is my_list2[4])

"""
my_list1 => [1,2,3,4, 👇]
                    [5, 6]
                    
            [1,2,3,4, 👇] <= my_list2
                    [5, 6]

my_list2[4].append(7)

my_list1 => [1,2,3,4, 👇]
                    [5, 6]
                    
            [1,2,3,4, 👇] <= my_list2
                    [5, 6, 7]
"""