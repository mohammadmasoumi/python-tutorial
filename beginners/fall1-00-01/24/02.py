

my_list = [(1, 2), (1, 1), (2, 1), (2, 2), (1, 0)]


def my_cutome_sort_func(item):

    x, y = item

    return x**2 + y**2


my_list.sort(key=my_cutome_sort_func)
print(my_list)
