import sys

my_list = []
my_tuple = ()

# the size of object in bytes.
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))

for i in range(100):
    size_before = sys.getsizeof(my_list)
    my_list.append(i)
    size_after = sys.getsizeof(my_list)

    print(f"diff: {size_after - size_before}, size_after: {size_after}, size_before: {size_before}")
