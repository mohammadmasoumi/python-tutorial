import sys

my_list = []
id(my_list)

prev = sys.getsizeof(my_list)

# [start:End:step]
# range(start, end(not included): step)

# index: [0, ..., 99]

# my_list: [0]
# my_list: [0, 1]
for idx in range(100):
    # idx: 0, [0]
    my_list.append(idx)
    curr = sys.getsizeof(my_list)
    # [0, 1, 2], []
    print(f"idx: {idx} | diff: {curr - prev}: size: {curr}")

    prev = curr
