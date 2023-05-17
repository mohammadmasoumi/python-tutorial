import sys
import time

t1 = (1, 2, 3, 4)
l1 = [1, 2, 3, 4]

print(sys.getsizeof(t1))  # 72 bytes
print(sys.getsizeof(l1))  # 88 bytes

print("----------------------------")

my_list = []
for idx in range(100):
    time.sleep(0.5)
    before = sys.getsizeof(my_list)
    my_list.append(idx)
    after = sys.getsizeof(my_list)

    print(
        f"before: {before} bytes | after: {after} bytes | diff: {after-before} bytes")
