# Q7

my_list = [[5, 10, 9], [6, 7, 1]]

my_new_list = [item ** 2 if item % 3 else item * 2 for items in my_list for item in items]

print(my_new_list)
"""
output:

[25, 100, 18, 12, 49, 1]
"""
