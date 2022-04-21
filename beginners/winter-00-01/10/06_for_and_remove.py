my_list = [1, 2, 3, 4]

# index: 0, my_list: [1, 2, 3, 4]
# elem: my_list[index]
# elem: my_list[0] - 1
# ----------------------
# index: 1, my_list: [2, 3, 4]
# elem: my_list[index]
# elem: my_list[0] - 3
# ----------------------
# index: 2, my_list: [2, 4]
# elem: my_list[index] ? Exit for loop

for elem in my_list:
    # elem: 1
    # elem: 3
    my_list.remove(elem)
    # my_list: [2, 4]
    print(elem, my_list) 
    # 1
    # 3

print(my_list)
print("------------------")