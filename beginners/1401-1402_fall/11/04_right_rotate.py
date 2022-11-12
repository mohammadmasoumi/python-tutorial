"""
n: 1
n: 6

-5-4-3-2-1
0 1 2 3 4
----------
1 2 3 4 5
----------
n:1 [5] [1 2 3 4] => [-1:] + [:-1]
n:2 [4 5] [1 2 3] => [-2:] + [:-2]
n:3 [3 4 5] [1 2]
n:4 [2 3 4 5] [1]
n:5 [1 2 3 4 5]
n:6 [5] [1 2 3 4]
"""
n_rotate = int(input())
my_list = [1, 2, 3, 4, 5]


# my_list = [1, 2, 4, 5]
# item = my_list.pop(2)
# item: 3

# 1.
# for _ in range( n_rotate % len(my_list)):
#     # item = my_list.pop()
#     my_list.insert(0, my_list.pop())
# print(my_list)

# 2.
n_rotate = n_rotate % len(my_list)
print(my_list[-n_rotate:] + my_list[:-n_rotate])
