# fruits = ["apple", "orange", "banana"]
my_list1 = [[1, 2], [3, 4]]
my_list2 = [1, 2, 3, 4]

# print(my_list1[0])
# print(my_list1[1])
# print(my_list1[0][0])
# print(my_list1[0][1])
# print(my_list1[1][0])
# print(my_list1[1][1])
# print(my_list2[0])

# my_list1 = [[1, 2], [3, 4]]
my_list3 = [[1, 2, 3], [4, 5, 6]]
for item in my_list3:
    # print(item)
    # item = [1, 2]
    # a, b = [1, 2]
    #  not enough values to unpack (expected 3, got 2)
    # [1, 2, 3]
    a, b, c = item
    print(f"a: {a}, b: {b}, c: {c}, item: {item}")

print("--------------------------------")
for a, b, c in my_list3:
    # print(item)
    # item = [1, 2]
    # a, b = [1, 2]
    #  not enough values to unpack (expected 3, got 2)
    # [1, 2, 3]
    print(f"a: {a}, b: {b}, c: {c}")

print("--------------------------------")
fruits = ["apple", "orange", "banana"]
# enumerate creates a 2d array of index and element
# (index, element)
# enumerate => [(0, 'apple'), (1, 'orange'), (2, 'banana')]
for item in enumerate(fruits):
    idx, fruit = item
    print(f"idx: {idx}, fruit: {fruit}, item: {item}")

print("--------------------------------")
for idx, fruit in enumerate(fruits):
    print(f"idx: {idx}, fruit: {fruit}")
