# sort
my_list = [0, -49, 1, 50, 51, 49]

# my_list = [0, -49, 1, 50, 51, 49]
#            50  99  49  0  1   1
#            50, 51, 49 , 1. 0. -49
# 
# .sort() function
def my_sort(value):
    return abs(value - 50)

my_list.sort()
print(my_list)

my_list.sort(key=my_sort)
print(my_list)

my_list.sort(key=my_sort, reverse=True)
print(my_list)

