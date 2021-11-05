import sys
from time import sleep
# from datetime import *
# from datetime import datetime, timedelta

# +3:30
# print(datetime.utcnow())
# print(datetime.now())
# print(datetime.now() - timedelta(hours=2))

# from .my_import import asghar


my_list = []
print(id(my_list))
# the size of object in bytes.
print(sys.getsizeof(my_list))  # 56 bytes 56 * 8 bits

prev = 0

# range(20) -> 0, 1, ..., 18, 19
# range(start, end, step)
for idx in range(100):
    my_list.append(idx)
    # curr = 56, prev = 0
    # curr = 100, prev = 56
    curr = sys.getsizeof(my_list)
    sleep(1)
    print(f"idx: {idx} | len: {len(my_list)} | diff: {curr - prev}: size: {curr}")

    # prev = 56
    prev = curr
