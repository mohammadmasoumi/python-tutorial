import sys
import time

my_int = 12
my_list = []
my_tuple = tuple()

print(sys.getsizeof(my_int)) # 28 bytes
print(sys.getsizeof(my_list)) # 56 bytes
print(sys.getsizeof(my_tuple)) # 40 bytes


for idx in range(100):
    before = sys.getsizeof(my_list)
    my_list.append(idx)
    after = sys.getsizeof(my_list)
    
    time.sleep(0.5)
    print(f"before: {before} | after: {after} | diff: {after - before}")