

# my_list = [[[[[1, 2]]]], [3, 4]]
my_list = [[1, 2], 3, 4]


def walk(item):
    # item: [[1, 2], 3, 4]

    if not isinstance(item, (list, tuple, set)):
        print(item)
        return item
    else:
        for elem in item:
            # elem: 1
            walk(elem)


# print(walk(10))
walk(my_list)
