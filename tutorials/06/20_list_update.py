my_list = []

for idx in range(100):
    my_list.append(idx)

print("---------------------------------")
for idx, item in enumerate(range(100)):
    my_list[idx] = item + 2

print("---------------------------------")
my_list1 = [[1, 2], [3, 4]]
