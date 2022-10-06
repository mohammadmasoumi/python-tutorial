a_list1 = range(10)

# filter
# map
# at the same time
a_list2 = [item * 2 for item in a_list1 if item != 2]

# old fashion
a_list3 = []
for item in a_list1:
    # item = item * 2

    # if I want to change items on the list
    # a_list1[idx] = item * 2

    a_list3.append(item * 2)


# my_func()
def my_func(elem):
    # return print(abs(elem - 50))
    # return abs(elem - 50)

    # print(elem)

    # print(abs(elem - 50))
    # return print(abs(elem - 50))
    # return None
    return elem * 2


# print(my_func(10))
# print(a)
# my_func(10)
# [0, 1 , 2, 9]
a_list4 = list(map(my_func, range(10)))
# print(a_list4)

# Stops when the shortest iterable is exhausted.
a_map = map(my_func, range(10))

#
# print("with next", next(a_map))
# for idx, item in enumerate(a_map):
#     print(idx, item)
#
# # disposal list
# for idx, item in enumerate(a_map):
#     print("Heyyyyyyyyyyyyyyyyyyyy")
#     print(idx, item)

# print(next(a_map))
# print(next(a_map))
# print(next(a_map))
# print(next(a_map))
# print(next(a_map))
