my_list = [12, 13, 14, 15]


#                        method, iterator
#                        method, my_list
def double(item):
    return item * 2


# method
# method() call, invoke

# TypeError: 'int' object is not callable
# double_my_list = list(map(double(12), my_list))
# double_my_list = list(map(24, my_list))
# double_my_list = list(map(24(item), my_list))

double_my_list = list(map(double, my_list))
print(double_my_list)
print(my_list)
