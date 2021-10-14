a_list = [[2, 1], [2, 3], [3, 2], [3, 4]]


def my_order(item):
    return item[1]


a_list.sort(key=my_order)
print(a_list)
