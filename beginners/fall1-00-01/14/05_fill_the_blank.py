my_list = [1, None, 2, 2, None, 3, None]

for idx, item in enumerate(my_list):
    # if item == None:
    # idx: 1, item: None
    if not item:
        my_list[idx] = my_list[idx - 1]

print(my_list)
