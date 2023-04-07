my_list = [1, 2, 3, 4]

# pointer: 0, 1, 2
for item in my_list: # [2, 3, 4], [2, 4]
    # item: 1, my_list[pointer]
    # item: 3, my_list[1]: 3
    my_list.remove(item)
    # my_list: [2, 3, 4]
    # my_list: [2, 4]
    print(item) # print(1) , print(3)

# Terminal
# 1
# 3
# [2, 4]

print(my_list)

# [2, 4]

# for item in my_list:
#     my_list.append(item)
#     print(item)

#          0
my_list = [1, 2, 3, 4]

#            0
# my_list = [2, 3, 4]

# pointer: 0
# index: 0
for item in my_list:
    # item: my_list[index], my_list[pointer]
    my_list.remove(item)
    print(item) 
