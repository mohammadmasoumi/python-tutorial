my_list = [1, 2, 3, 4, 5]


for item in my_list:
    print(item)

for idx in range(len(my_list)):
    # idx: idx
    # item: my_list[idx]
    print(my_list[idx])

counter = 0
for item in my_list:
    print(my_list[counter])
    counter += 1

print("*****************")
# idx item
# (0, 1)
# (1, 2)
# (2, 3)
# (3, 4)
# (4, 5)
for elem in enumerate(my_list):
    # idx, item = elem
    # idx. item = (0, 1)
    # idx: 0, item: 1
    print(elem)

print("*****************")
# idx -> value
for idx, item in enumerate(my_list):
    print(idx, item)