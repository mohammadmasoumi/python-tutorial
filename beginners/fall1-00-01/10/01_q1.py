# به هر المان مای لیست یک واحد اضافه کنید.

my_list = [
    [1, 2, 3],
    [4, 5, 6]
]

for item in my_list:
    # item = [1, 2, 3]  avalin bar
    # item = [2, 2, 3]  dovomin bar

    #  cannot unpack non-iterable int object
    for idx, a in enumerate(item):
        # idx = 1, a = 2
        a += 1  # a = 3
        # update element in list
        item[idx] = a  # item = [3, 2, 3]

print(my_list)
