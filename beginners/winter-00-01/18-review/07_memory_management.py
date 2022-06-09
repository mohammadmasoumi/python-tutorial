import sys

my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)

print(sys.getsizeof(my_list)) # 120 Bytes
print(sys.getsizeof(my_tuple)) # # 74 Bytes


for num in range(100):
    before = sys.getsizeof(my_list)
    my_list.append(num)
    after = sys.getsizeof(my_list)

    print(f"before: {before}, after: {after}, diff: {after - before}")