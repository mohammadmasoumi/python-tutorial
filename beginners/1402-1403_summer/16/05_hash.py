import time
rand = int(time.time())


def my_hash(value):
    if isinstance(value, int):
        return value
    elif isinstance(value, (str, float)):
        return sum([ord(char) * (idx + 1) for idx, char in enumerate(str(value))]) * rand
    elif isinstance(value, tuple):
        return sum([(idx + 1) * my_hash(item) for idx, item in enumerate(value)]) * rand
    elif isinstance(value, (list, set)):
        raise ValueError(f'{type(value)} is not hashable')


print(my_hash(12))
print(my_hash(12))
print(my_hash(12.2))
print(my_hash("ali"))
print(my_hash("ali"))
print(my_hash(("ali", 12)))
# ValueError: <class 'list'> is not hashable
# print(my_hash(("ali", [12, 2])))
