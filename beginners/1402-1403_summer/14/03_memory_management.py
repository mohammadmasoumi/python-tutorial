import sys
import time

"""
list: mutable 
tuple: immutable 
"""
# use the `sys. getsizeof()` function to determine the size of an object in byte

my_tuple = (1, 2, 3, 4)
my_list = [1, 2, 3, 4]

"""
0 -> 1
1 -> 2
2 -> 3
3
############################
my_list = [1, 2, 200]
my_tuple = [1, 2, 200]
--------------------
list: 5
index 
[x56][x60][x160][][]
--------------------
tuple: 3
index 
[x56][x60][x160]
--------------------
x56     x60    x160
[2]     [1]    [200]
"""
print(sys.getsizeof(my_tuple))
print(sys.getsizeof(my_list))

# my_list = []
# for i in range(25):
#     before = sys.getsizeof(my_list)
#     my_list.append(i)
#     after = sys.getsizeof(my_list)

#     diff = after - before

#     time.sleep(1)

#     # 1 byte -> 8 bits
#     # int
#     # 32 bits
#     # 12 -> 1100
#     # 000000000000000000000000000000000000000000000000000000000000001100
#     # actual_size = len(my_list) * sys.getsizeof(i)
#     # actual_size: {actual_size},
#     print(f"before: {before} bytes, after: {after} bytes, diff: {diff}")
