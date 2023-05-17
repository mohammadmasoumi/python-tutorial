# methods on list

my_list = [1, 2, 3, 4, 5]

my_list.append(6)
my_list.extend("ali")  # iterable
my_list.insert(0, 10)
my_list.remove(2)  # item
item = my_list.pop()  # index
item = my_list.pop(2)  # index
my_list.clear()

my_list2 = [1, 2, 3, 4]
my_list3 = [1, 2, 3, 4]

my_list2.append([5, 6, 7])
my_list3.extend([5, 6, 7])

print(my_list2)  # [1, 2, 3, 4, [5, 6, 7]]
print(my_list3)  # [1, 2, 3, 4, 5, 6, 7]

# methods on tuple
print("--------------------------------")
my_tuple = (1, 2, 3, 4, 1)

print(my_tuple.count(1))
#                   element, start, stop
#           find element in [start, end) range
print(my_tuple.index(1, 1))
