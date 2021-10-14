import sys

# print(sys.getsizeof([]))
# print(sys.getsizeof([1]))
# print(sys.getsizeof([1, 2]))
# print(sys.getsizeof([1, 2, 3]))
# print(sys.getsizeof([1, 2, 3, 4]))
# print(sys.getsizeof([1, 2, 3, 4, 5]))
# print(sys.getsizeof([1, 2, 3, 4, 5, 6]))
# print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7]))
# print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8]))
# print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

my_llist = []
prev_size = 0

for idx in range(100):
    s = sys.getsizeof(my_llist)
    print(f"size of list with {len(my_llist)} elements is: {s} bytes | diff: {s - prev_size}")
    prev_size = s
    my_llist.append(idx)

print("--------------------------------------")

# for idx in range(10000, 100000):
#     my_list = list(range(idx))
#     my_tuple = tuple(range(idx))
#
#     print(f"length of list with {len(my_list)} items is: {sys.getsizeof(my_list)}")
#     print(f"length of tuple with {len(my_tuple)} items is: {sys.getsizeof(my_tuple)}")
