my_list = [1, 2, 3, 4, 5]

# index: 0
iterator = iter(my_list)

for item in iterator:
    # item = next(iterator)
    # index: 1

    if item > 2:
        break

# index: 2
my_list.remove(3)
# my_list = [1, 2, 4, 5]
print(next(iterator))  # 5

# --------------------------
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)  # item: 1, item: 3, item: 5
    # my_list: [2, 3, 4, 5], my_list: [2, 4, 5], my_list: [2, 4]
    my_list.remove(item)

print(my_list)
