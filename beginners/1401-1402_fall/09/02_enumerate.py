
my_list = [1, 2, 3, 4]

for index, item in enumerate(my_list):
    my_list[index] = item + 1

print(my_list)

my_list = [[1, 2], [3, 4]]

for item in my_list:
    item.insert(0, 10)

print(my_list)