my_list = [[1, 2], [3, 4], [5, 6]]

# print(my_list[0][0])
# print(my_list[0].append(10))

for elem in my_list:
    # [[1, 2], [3, 4], [5, 6]]
    # my_list2 = my_list.append(10)
    # my_list2: [[1, 2], [3, 4], [5, 6], 10]
    # ------------------------------------
    # my_list[0].append(10)
    # [[1, 2, 10, 10, 10], [3, 4], [5, 6]]
    # ------------------------------------
    elem.append(10)

print(my_list)