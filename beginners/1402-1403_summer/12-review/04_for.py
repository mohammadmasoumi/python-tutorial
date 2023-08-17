
my_list = [1, 2, 3, 4, 5, 6]

# 1. 
for item in my_list:
    # item: 1
    # item: 2
    # item: 3
    # item: 4
    # ...

    # -- for block
    print(item)

    # -- for block
    
# 2. 
my_list = [1, 2, 3, 4, 5, 6]

for item in my_list:
    # item: 1, index: 0, my_list: [1, 2, 3, 4, 5, 6]
    # item: 3, index: 1, my_list: [2, 3, 4, 5, 6]
    # item: 5, index: 2, my_list: [2, 4, 5, 6]
    # item: ?, index: 3, my_list: [2, 4, 6] -> StopIteration -> break for loop
    my_list.remove(item) # remove specified item from list
    # item: 1, my_list: [2, 3, 4, 5, 6]
    # item: 3, my_list: [2, 4, 5, 6]
    # item: 5, my_list: [2, 4, 6]

print(my_list)

# 3. infinite loop 
my_list = [1, 2, 3, 4, 5, 6]

for item in my_list:
    # item: 1, index: 0, my_list: [1, 2, 3, 4, 5, 6]
    # item: 2, index: 1, my_list: [1, 2, 3, 4, 5, 6, 1]
    # item: 3, index: 2, my_list: [1, 2, 3, 4, 5, 6, 1, 2]
    my_list.append(item)
    # item: 1, index: 0, my_list: [1, 2, 3, 4, 5, 6, 1]
    # item: 2, index: 1, my_list: [1, 2, 3, 4, 5, 6, 1, 2]
    # item: 3, index: 2, my_list: [1, 2, 3, 4, 5, 6, 1, 2, 3]


print(my_list)