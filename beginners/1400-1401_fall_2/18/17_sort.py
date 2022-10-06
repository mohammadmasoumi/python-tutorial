# sort
my_dict = {"d": 2, "a":10, "b":3 , "c":20}

# [].sort(key=function, reverse=True)

def my_sort(item):
    # item: ('d', 4)
    # item: ('a', 1)
    # item: ('b', 2)
    # item: ('c', 3)
    #        tuple
    #       key, value
    # key = item[0]
    # value = item[1]
    key, value = item
    return value


def my_sort2(item):
    # item: ('d', 4)
    # item: ('a', 1)
    # item: ('b', 2)
    # item: ('c', 3)
    #        tuple
    #       key, value
    # key = item[0]
    # value = item[1]
    key, value = item
    return key

def my_sort3(item):
    # item: ('d', 4)
    # item: ('a', 1)
    # item: ('b', 2)
    # item: ('c', 3)
    #        tuple
    #       key, value
    # key = item[0]
    # value = item[1]
    key, value = item
    return abs(50 - value)

print(my_dict.items())
#         key, value = ('d', 4)
# dict_items([('d', 4), ('a', 1), ('b', 2), ('c', 3)])

print(my_dict)
print(dict(sorted(my_dict.items(), key=my_sort)))
print(dict(sorted(my_dict.items(), key=my_sort2)))
print(dict(sorted(my_dict.items(), key=my_sort3)))
print(dict(sorted(my_dict.items(), key=my_sort3, reverse=True)))

