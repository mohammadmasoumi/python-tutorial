my_list1 = [
    [10, 20, 30],
    [11, 12, 13]
]
# = my_list2 [10, 20, 30, 11, 12, 13]

my_list2 = []

for item in my_list1:
    for a in item:
        my_list2.append(a)

print(my_list2)
print(sum(my_list2))
