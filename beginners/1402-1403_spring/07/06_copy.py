
my_list1 = [1, 2, 3, 4]
my_list2 = my_list1


"""
    my_list
        |
        [1, 2, 3, 4]
        |
    my_list2

"""

my_list2.append(5)

print(my_list1) # [1, 2, 3, 4, 5]
print(my_list2) # [1, 2, 3, 4, 5]


my_list1 = [1, 2, 3, 4]
my_list2 = my_list1.copy()


"""
Shallow copy

    my_list
        |
        [1, 2, 3, 4]

    my_list2
        |
        [1, 2, 3, 4, 5]
"""

my_list2.append(5)

print(my_list1) # [1, 2, 3, 4]
print(my_list2) # [1, 2, 3, 4, 5]


"""
Deep copy

    Problem:
        my_list
            |
            [1, 2, 3, 4, ]
                        |
                    [5, 6]
                        |
        my_list2        |
            |           |
            [1, 2, 3, 4, ]

    Solution:
        my_list
            |
            [1, 2, 3, 4, ]
                        |
                    [5, 6]

                    [5, 6]
                        |
        my_list2        |
            |           |
            [1, 2, 3, 4, ]
"""
from copy import deepcopy

my_list1 = [1, 2, 3, 4, [5 , 6]]
my_list2 = deepcopy(my_list1)

my_list2[4].append(7)

print(my_list1) # [1, 2, 3, 4]
print(my_list2) # [1, 2, 3, 4, 5]