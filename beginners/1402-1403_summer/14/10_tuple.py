#
my_list = [1, 2, 3]
my_tuple = (1, 2, my_list)  # (1, 2, [1, 2, 3])

my_list.append(4)
print(my_tuple)

my_list = [10, 12, 13]
print(my_tuple)

"""
1.

my_list ->  [1, 2, 3]
                   ^
                   |
my_tuple -> (1, 2, *)

2.
my_list ->  [10, 11, 12]
               [1, 2, 3]
                   ^
                   |
my_tuple -> (1, 2, *)
"""
