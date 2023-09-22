# print(hash("ali"))
# print(hash("ali"))
import time
rand = int(time.time())


def my_hash(value):  # index
    if isinstance(value, int):
        return value
    elif isinstance(value, (str, float)):
        # "ila" "ali"
        # "asghar"
        # chr("a") * (1) + chr("l") * (2) + chr("i") * (3)
        # chr("i") * (1) + chr("l") * (2) + chr("a") * (3)
        return sum([ord(char) * (idx + 1) for idx, char in enumerate(str(value))]) * rand
    elif isinstance(value, tuple):
        # (1, "ali", 2.2)
        # (2.2, "ali", 1)
        # (2.2, ("ali", 1))
        for idx, item in enumerate(value):
            my_hash(item)

    elif isinstance(value, (list, set)):
        raise ValueError(f'{type(value)} is not hashable')


print(my_hash(12))
print(my_hash(12.2))
print(my_hash(12.3))
print("---------------")
print(my_hash("ali"))
print(my_hash("ali"))
print(my_hash("ila"))
print("---------------")
