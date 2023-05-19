# application
import time

my_list = [1, 2, 3, 4, 5, 2, 3, 4]

print(list(set(my_list)))


my_list1 = list(range(10000))
my_list2 = list(range(100, 10000))

s = time.perf_counter()
list(set(my_list1).intersection(set(my_list2)))
t = time.perf_counter()
print(f"Duration: {t-s} seconds")

# s = time.perf_counter()
# intersection = []
# for item1 in my_list1:
#     # if item1 in my_list2:
#     #     intersection.append(item1)
#     for item2 in my_list2:
#         if item1 == item2:
#             intersection.append(item2)
#     # intersection.append(item1) if item1 in my_list2 else None

# t = time.perf_counter()

# print(f"Duration: {t-s} seconds")
