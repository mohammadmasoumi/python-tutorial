import sys
import time

my_list = []

for i in range(20):
    size_before = sys.getsizeof(my_list)
    my_list.append(i)
    size_after = sys.getsizeof(my_list)
    time.sleep(0.5)
    print(f"before: {size_before}, after: {size_after}, diff: {size_after - size_before}")