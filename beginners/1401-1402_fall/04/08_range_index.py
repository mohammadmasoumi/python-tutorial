# range index

#         -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#          0  1  2  3  4  5  6  7  8  9
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# normal index
# [index]
# [0: len-1]
# IndexError: list index out of range
# print(my_list[100])

# range index
# [start(included): end(not included): step]

# default step: +1
print(my_list[1:4]) # [2, 3, 4]
print(my_list[1:4: 2]) # [2, 4]
print(my_list[-1: -10: -1])
print(my_list[-1: -100: -1])

# 
print(my_list[:6]) # [1, 2, 3, 4, 5, 6]
print(my_list[:6:-1]) # [10, 9, 8]

# 
print(my_list[1::-1]) # [2, 1]
print(my_list[4::1]) # [5, 6, 7, 8, 9, 10

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(my_list[::-3]) # [10, 7, 4, 1]
print(my_list[::]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# reverse list
print(my_list[::-1])