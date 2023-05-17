my_list = [1, 2, 3, 4, 5]

# index: 0
iterator = iter(my_list)

for item in iterator:
    # item = next(iterator)
    # index: 1

    if item > 2:
        break

# index: 2
my_list.insert(0, 10)
# my_list = [10, 1, 2, 3, 4, 5]
print(next(iterator))  # index: 3 item: 3
print(next(iterator))  # index: 4 item: 4
