# sort

my_list = [-1, 49, 0, 50, 51]
"""
-1       ...     49 50  
-O----------------O-O---------------------

formula
abs(x - 50)
| x - 50 |

[0, 1,  1,  50, 51] distance from 50
[50, 51, 49, 0, -1] actual items
"""

# def sort_function(item):
#     return abs(50 - item)

#       function, reverse
# my_list.sort(key=sort_function)
my_list.sort(key=lambda x: abs(x - 50))

print(my_list)
# my_list = [-1, 49, 0, 50, 51]
# sort_base_on = []
# for item in my_list:
#     res = sort_function(item)
#     sort_base_on.append((item, res))

# print(sort_base_on)
# [(-1, 51), (49, 1), (0, 50), (50, 0), (51, 1)]
# [(50, 0), (49, 1), (51, 1), (0, 50), (-1, 51)]
# [50, 49, 51, 0, -1]

my_list = [100, 49, 18, 53, 55]
my_list.sort(key=lambda x: x%10, reverse=True)
my_list.sort(key=lambda x: x, reverse=True)
# [100, 53, 55, 18, 49]
print(my_list)

print(sorted(my_list))

my_list = [-1, 1, 2, -10]
my_list.sort(key=lambda x: x)
print(my_list)

my_list = [-1, 1, 2, -10]
my_list.sort(key=lambda x: str(x))
print(my_list)

# "-10"
# "10"

