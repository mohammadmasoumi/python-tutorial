# my_hash
import time

# bool -> int
# bool is the subset of int
# so you must check bool first

rand = time.time()

# 1, 2, (3, 4), 5
#        |  ^
#        V  |
#        3, 4

def walk(item):
    if isinstance(item, (list, set)):
        raise ValueError(f'unhashable type {type(item)}')

    if isinstance(item, tuple):
        for elem in item:
            # elem: 1
            walk(elem)


walk((1, 2, (3, 4), 5))


def my_hash(n):
    # n: (4, 5, [1, 2, 3])
    # n: 4

    if isinstance(n, bool):
        return int(n)  # return 1 if n else 0
    elif isinstance(n, int):
        return n
    elif isinstance(n, str):
        # return sum([ord(char) for char in n])
        return sum([(idx+1)*ord(char) for idx, char in enumerate(n)]) * rand
    elif isinstance(n, list):
        raise ValueError('unhashable type list')
    elif isinstance(n, set):
        raise ValueError('unhashable type set')
    elif isinstance(n, tuple):
        # n: (4, 5, [1, 2, 3])
        # elem: 4, my_hash(4): 4
        # elem: 5, my_hash(5): 5
        # elem: [1, 2, 3], my_hash([1, 2, 3]) -> raise exception
        # [1*4, 2*5, ]
        return sum([(idx+1)*my_hash(elem) for idx, elem in enumerate(n)]) * rand


print(my_hash((1, 2, 3)))
# print(my_hash((4, 5, [1, 2, 3])))

# 1*(1*1+2*2)+2*(1*(3*1+4*2)+2*5)+3*6
h1 = ((1, 2), ((3, 4), 5), 6)
print(my_hash(h1))

# print(my_hash(1))
# print(my_hash(12))

# print(my_hash(True))
# print(my_hash(False))

# print(my_hash("lia"))
# print(my_hash("ila"))
# print(my_hash("ali"))

# for item in range(10):
#     pass
#     time.sleep(0.1)

# print(my_hash("ali"))
# print(my_hash([1, 2, 3]))
