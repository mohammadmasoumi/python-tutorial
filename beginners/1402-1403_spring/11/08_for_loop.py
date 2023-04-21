# for each

my_list = [1, 2, 3, 4]

# for item in my_list:
#     print(item)

# index: 0
# item: my_list[index]
for item in my_list:
    # item: 1, index: 0, my_list: [1, 2, 3, 4]
    # item: 3, index: 1, my_list: [2, 3, 4]
    # item: StopInteration, index: 2, my_list: [2, 4]
    print(item)
    my_list.remove(item) # value
    # item: 1, index: 0, my_list: [2, 3, 4]
    # item: 3, index: 1, my_list: [2, 4]

print(my_list)

"""
1
3
[2, 4]
"""