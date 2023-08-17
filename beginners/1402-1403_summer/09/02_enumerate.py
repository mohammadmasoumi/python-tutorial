# enumerate 
# [0:len-1]
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    # item = my_list[index]
    print(item)

index = 0
for item in my_list:
    print(my_list[index])
    index += 1

# end: len(my_list)
# [0: len(my_list)-1]
for idx in range(len(my_list)):
    item = my_list[idx]

    # update
    my_list[idx] = item + 2

# 3.
my_list = [1, 2, 3, 4, 5]
# idx value/item
# (0, 3)
# (1, 4)
# (2, 5)
# (3, 6)
# (4, 7)

# idx, item = (0, 3)

# unpacking/packing
a, b = 10, 12
# a=10, b=10
a, b = (10, 12)
# a=10, b=10

for elem in enumerate(my_list):
    # idx, item = elem
    # idx, item = (0, 3)
    # idx: 0, item: 3
    idx, item = elem # unpack
    print(f"idx: {idx}, item: {item}, elem: {elem}")


for idx, item in enumerate(my_list):
    print(idx, item)