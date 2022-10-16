my_list = [12, 19, 6, 1, 5, 10]

# ctrl + a => select all
# ctrl + alt + l => pretty

for i in range(len(my_list)):
    min_index = -1
    min_item = 1000
    for idx in range(i, len(my_list)):
        if my_list[idx] < min_item:
            min_item = my_list[idx]
            min_index = idx

    # swap
    my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

print(my_list)
