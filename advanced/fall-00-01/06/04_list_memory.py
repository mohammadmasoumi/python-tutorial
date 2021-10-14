import sys

my_list = []
id(my_list)

prev = 0
for idx in range(100):
    my_list.append(idx)
    curr = sys.getsizeof(my_list)
    print(f"idx: {idx} | diff: {curr - prev}: size: {curr}")
    prev = curr
