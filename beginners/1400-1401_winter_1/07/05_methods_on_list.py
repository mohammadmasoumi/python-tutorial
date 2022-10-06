# methods on list

# list attr
my_list = [1, 2, 3, 4]

# 1. Changeable - mutable
my_list.append(5)

# 2. Accept duplicate element
my_list = [1, 1, 2, 3, 4] 

# 3. Ordered
print(my_list)

# --------------------------------
# clear - Removes all the elements from the list
my_list.clear()

print(my_list)

# count - Returns the number of elements with the specified value
my_list = [1, 1, 1, 2, 3, 4] 
print(my_list.count(1))

# index - Returns the index of the first element with the specified value
# my_list.index(1) | value -> index
# my_list[0] | index -> value
print(my_list.index(1))
#                  value start stop
print(my_list.index(1, 1, 10))
# ValueError: 1 is not in list
# print(my_list.index(1, 3, 10))

# reverse - Reverses the order of the list
print(my_list.reverse())
# print(my_list.pop())
print(my_list)
