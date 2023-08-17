my_list = [9, 2, 9.9, 8]

# +10

"""

                2     8  
                ^     ^
                |     |
my_list --> [*, *, *, *]
             |     |
             v     v
             9     9.9
             ^
             X
             |
            item
             |
             v
             19
"""

# my_list = [9, 2, 9.9, 8]
index = 0
for item in my_list:
    # item: my_list[index]
    # item.update(item+10)
    # my_list[index] = item + 10
    my_list[index] += 10
    index += 1


# my_list = [9, 2, 9.9, 8]
for item in my_list:
    # item: my_list[0] | int
    # item = my_list[0]
    # item = item + 10
    item += 10
    # item.update(item+10)
    my_list[0] += item

my_list = [9, 2, 9.9, 8]
for item in my_list:
    # item: 9
    # item: 2
    # item: 9.9
    # item: 8
    item += 10
    # item: 19
    # item: 12
    # item: 19.9
    # item: 18
    # my_list[0] = my_list[0] + item
    # my_list[0] = 9 + 19
    # my_list[0] = 28 + 12
    # my_list[0] = 40 + 19.9
    # my_list[0] = 59.9 + 18
    # my_list: [28, 2, 9.9, 8]
    # my_list: [40, 2, 9.9, 8]
    # my_list: [59.9, 2, 9.9, 8]
    # my_list: [77.9, 2, 9.9, 8]
    my_list[0] += item


print(my_list)
