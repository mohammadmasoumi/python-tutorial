# enumerate

my_list = [1, 2, 3, 4]
for elem in enumerate(my_list):
    # elem: (index, item)
    # index, item = (index, item)
    index, item = elem

    print(index, item, elem) # (index, item)