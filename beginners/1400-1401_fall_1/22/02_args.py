"""



"""


def add_multi_values(*items):
    # print(items)

    return sum(items)
    # s = 0
    # for i in range(len(items)):
    #     s += i
    #
    # return s


print(add_multi_values(10, 12, 13, 14))
print(add_multi_values(10, 12))
print(add_multi_values(10, 12, 20, 21, 22, 23))


def add_multi_values2(a, *items):
    print(a, items)

    return sum((a,) + items)


# TypeError: add_multi_values3() missing 1 required keyword-only argument: 'c'
#                        *args
def add_multi_values3(a, *items, c):
    # items: tuple
    print(a, items, c)

    return sum((a,) + items)


print("res: ", add_multi_values3(10, 12, 13, 14, c=12))
print("res: ", add_multi_values3(10, 12, c=12))
print("res: ", add_multi_values3(10, 12, 20, 21, 22, 23, c=12))


#                        **kwargs
def add_multi_key_values(**items):
    # items: dict
    print(items)
    for key, value in items.items():
        print(key, value)


print("res: ", add_multi_key_values(key="name", value="ali", age=20))
# print("res: ", add_multi_key_values())
# print("res: ", add_multi_key_values())
