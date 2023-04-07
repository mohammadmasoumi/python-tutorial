# slicing
# range index

#         -4 -3 -2 -1    [-len:-1]
#          0  1  2  3    [0:len-1]
my_list = [1, 2, 3, 4]
# 

# index => ONE element
print(my_list[0], my_list[2])
print(my_list[-4], my_list[-2])

# slicing => []
# [start:end:step]
print(my_list[0:3:2])
print(my_list[::2])
print(my_list[::-2]) # [4, 2]

# cast
print(list("Hello"))