# 
my_list = [1, 2, 3, 4]

for item in my_list:
    # item: 1, index: 0, my_list: [1, 2, 3, 4]
    # item: 3, index: 1, my_list: [2, 3, 4]
    # item: ?, index: 2, my_list: [2, 4] StopIteration
    my_list.remove(item)
    # item: 1, index: 0, my_list: [2, 3, 4]
    # item: 3, index: 1, my_list: [2, 4]
    

print(my_list) # [2, 4]

# 1. -----------------
my_list.clear()

# 2. -----------------
my_list = [1, 2, 3, 4]
# create new list with the value previous list
copied_list = my_list.copy() # [1, 2, 3, 4]

# my_list = [1, 2, 3, 4]
# copied_list = [1, 2, 3, 4]
for item in copied_list:
    # item: 1, index: 0, copied_list: [1, 2, 3, 4], my_list: [1, 2, 3, 4]
    # item: 2, index: 1, copied_list: [1, 2, 3, 4], my_list: [1, 2, 3, 4]
    my_list.remove(item)
    # item: 1, copied_list: [1, 2, 3, 4], my_list: [2, 3, 4]
    # item: 2, copied_list: [1, 2, 3, 4], my_list: [3, 4]

# ------------
my_list = [1, 2, 3, 4]
for item in my_list:
    my_list.append(item)

print(my_list)