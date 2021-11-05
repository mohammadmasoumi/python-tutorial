my_list = [1, 2, 3, 4, 5]


def is_less_than_3(item):
    return item < 3


func1 = lambda x: x < 3
# func1()

# usage:
# filter, map
# inline function
# not reusable

print(id(is_less_than_3))
print(id(func1))

print(list(filter(is_less_than_3, my_list)))
print(list(filter(lambda x: x < 3, my_list)))
