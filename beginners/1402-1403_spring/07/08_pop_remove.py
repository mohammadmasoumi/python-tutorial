my_list = [1, 2, 3, 4]

# pop - index

item = my_list.pop() # last
# item: 4, my_list: [1, 2, 3]
item = my_list.pop(0) # index
# item: 1, my_list: [2, 3]

# remove - element - value
my_list.remove(2)
# my_list: [3]
print(my_list)

