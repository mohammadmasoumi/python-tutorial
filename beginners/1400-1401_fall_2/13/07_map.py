my_list = [12, 13, 14, 15]


def double(item):
    if item % 2 == 0:
        return item // 2
    else:
        return item * 2


double_my_list = list(map(double, my_list))
print(double_my_list)
print(my_list)
