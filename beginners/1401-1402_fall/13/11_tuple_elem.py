tuple1 = (1, True, "hello", [1, 2], 1.0, (1, ))
list1 = [(1, 2), (3, 4)]

print(tuple1)

my_list = [10, 20, 30, 40]

for item in enumerate(my_list):
    print(item, type(item))

for index, item in enumerate(my_list):
    print(index, item)