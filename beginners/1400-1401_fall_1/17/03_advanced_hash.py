"""
خروجی به شما bool میدهد.
bool = isinstance(item, int)
"""


def my_hash(item):
    # type(item) == int
    # if isinstance(item, str):
    # if isinstance(item, list):
    # if isinstance(item, dict):
    # if isinstance(item, float):
    # if isinstance(item, bool):
    if isinstance(item, int):
        return int(item)

    elif isinstance(item, str) or isinstance(item, tuple):
        return id(item)


# print(my_hash(12))
# print(my_hash("asghar agha"))
print(my_hash(True))
print(my_hash((1, 2, 3)))
print(int(True))
