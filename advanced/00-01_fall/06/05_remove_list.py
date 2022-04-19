my_list = [1, 2, 3, 4]

# just accept element - no index
my_list.remove(1)
print(my_list)

# index
my_list.pop(0)
print(my_list)
my_list.pop()
print(my_list)

# index
del my_list[0]
print(my_list)

# what is difference?
my_list = [1, 2, 3, 4]

# ValueError: list.remove(x): x not in list
# raise exception
# my_list.remove(11)

# IndexError: pop index out of range
# raise exception
# my_list.pop(10)

# IndexError: list assignment index out of range
# del my_list[10]
# del my_list
# print(my_list)
