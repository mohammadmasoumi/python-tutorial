# list

"""
 - Changeable/mutable
 - Ordered => index, indice
 - Duplicated is allowed

my_list[0] = 4
my_list[0]
[1, 1, 2] 

index range: [0 .. len-1]

"""
my_list = [1, 2, 3, 4, 5, 6]

# access
print(my_list[0])

# update
my_list[1] = 4

# del
del my_list[0]

# range index

"""
my_list = [1, 2, 3, 4, 5, 6]

end: not included
my_list[start:end:step]


"""

# range index
# positive index: [0: len-1]
# negative index: [-len: -1]
#          -6 -5 -4 -3 -2 -1
#          0  1  2  3  4  5
my_list = [1, 2, 3, 4, 5, 6]

print(my_list[-6])
print(my_list[0])

# slicing
# my_list[start:end:step]
# 
print(my_list[1])
