my_list = [1, 2, 3, 4, 5, 6]

"""
def filter(function: None, iterable: Iterable[Optional[_T]], /) -> Iterator[_T]
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""


def only_even(item):
    return not item % 2


def only_odd(item):
    return item % 2


def greater_than_2(item):
    return item > 2


# <filter object at 0x000001ED68A7B0A0>
# print(filter(only_even, my_list))
print(list(filter(only_even, my_list)))
print(list(filter(only_odd, my_list)))
print(list(filter(greater_than_2, my_list)))


# new_list = []

# for item in my_list:
#     result = only_even(item)
#     if result:
#         new_list.append(item)

my_list = ["baran", "bita", "bahar", "asghar"]


def starts_with_b(item):
    return item.startswith("b")


print(list(filter(starts_with_b, my_list)))
print(list(filter(lambda item: item.startswith("b"), my_list)))
