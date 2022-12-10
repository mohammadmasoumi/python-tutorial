import random


# module, library
import time

# time() -> floating point number
# Return the current time in seconds since the Epoch.
# Fractions of a second may be present if the system clock provides them.
random_number = time.time()
# random_number = random.randint(100, 1000000000)

# def hash_function(item):
#     # if isinstance(item, (int, float)):
#     if isinstance(item, (list, set, dict)):
#         raise ValueError(f"Unhashable type: ({type(item)})")

#     elif isinstance(item, (int, float)):
#         return item

#     elif isinstance(item, bool):
#         return 1 if item else 0

#     elif isinstance(item, str):
#         # ali , ila
#         hash_value = 0

#         # 97 + 1 + 98 + 2
#         # ab
#         # (a + index1 + 1) + (b + index2 + 1)
#         # (a + b) + (index1 + index2 + 2)
#         # 98 + 1 + 97 + 2
#         # ba
#         for idx, character in enumerate(item):
#             # ali
#             # bli
#             hash_value += ord(character) * (idx + 1) * random_number

#         return hash_value * 100

#     elif isinstance(item, tuple):
#         # ("a", "b")
#         # ("b", "a")
#         hash_value = 0

#         for idx, value in enumerate(item):
#             hash_value += hash_function(value) * (idx + 1) * random_number

#         return hash_value * 100


def hash_function(item):

    # if isinstance(item, (int, float)):
    if isinstance(item, (list, set, dict)):
        raise ValueError(f"Unhashable type: ({type(item)})")

    elif isinstance(item, (int, float)):
        return item

    elif isinstance(item, bool):
        return 1 if item else 0

    elif isinstance(item, str):
        # ali , ila
        hash_value = 0

        # 97 + 1 + 98 + 2
        # ab
        # (a + index1 + 1) + (b + index2 + 1)
        # (a + b) + (index1 + index2 + 2)
        # 98 + 1 + 97 + 2
        # ba
        for idx, character in enumerate(item):
            # ali
            # bli
            hash_value += ord(character) * (idx + 1) * random_number

        return hash_value * 100

    elif isinstance(item, tuple):
        # ("a", "b")
        # ("b", "a")
        hash_value = 0

        for idx, value in enumerate(item):
            hash_value += hash_function(value) * (idx + 1) * random_number

        return hash_value * 100


# int
print(hash_function(12))

# str
print("@li", hash_function("@li"))
print("@li", hash_function("@li"))
print("ali", hash_function("ali"))
print("ali", hash_function("ali"))
print("ial", hash_function("ial"))
print("ila", hash_function("ila"))

print("ali", hash_function("ali"))
print("bli", hash_function("bli"))

print("-------------------------")
print((1, 2), hash_function((1, 2)))
print((1, 2), hash_function((1, 2)))
print((2, 1), hash_function((2, 1)))
print((2, 1), hash_function((2, 1, (2, 1))))

print("-------------------------")
# print(([2, 1],), hash_function(([2, 1], )))

print((2, ), hash_function((2, )))
print(2, hash_function(2))

