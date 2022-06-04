my_list = [5, 20, 6, 10, 1, 2]


for rnd in range(len(my_list)):

    min_index = rnd
    min_item = my_list[rnd]

    for index in range(rnd, len(my_list)):
        item = my_list[index]

        if item < min_item:
            min_item = item 
            min_index = index

    my_list[rnd], my_list[min_index] = my_list[min_index], my_list[rnd]

        
print(my_list)
