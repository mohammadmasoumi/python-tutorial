# tuple

import time
import sys

my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

# 1 byte -> 8 bits
# 8*10^9 bits
print(sys.getsizeof(my_tuple))  # bytes
print(sys.getsizeof(my_list))  # 80 bytes -> 640 bits

"""
dynamic array
list -> mutable
    my_list.append(4)
    my_list.remove(4)

# memory efficiency

static array
tuple -> immutable
    tuple.count(4)
    tuple.index(4)
"""

# my_list = []

# for i in range(100):
#     time.sleep(1)

#     before = sys.getsizeof(my_list)
#     my_list.append(i)
#     after = sys.getsizeof(my_list)

#     print(f"before: {before}, after: {after}, diff: {after-before}")
my_tuple = (1, 2, 3, 4)

for item in my_tuple:
    print(item)


# int
my_tuple = (1)  # redundant paranthesis
# tuple
my_tuple = (1,)

my_tuple = ([1, 2, 3], 1, 2)

# TypeError: 'tuple' object does not support item assignment
# my_tuple[2] += 2

print(type(my_tuple[0]))

my_new_list = my_tuple[0]

my_tuple[0].append(10)
print(my_tuple)
my_tuple[0][0] *= 2
print(my_tuple)
my_new_list[0] *= 2
print(my_tuple)

# TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = tuple(my_tuple[0])

"""
pointer

(*, 1, 2)
 |
 |
 V
 [1, 2, 3, 10]

"""

my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)

my_tuple1 += my_tuple2
print(my_tuple1)

my_tuple = ((1, 2, 3), 1, 2)
