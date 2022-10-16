# shallow copy

my_list1 = [1, 2, 3]
my_list2 = my_list1.copy()
my_list1.append(5)
my_list2.append(4)

print(f"my_list1: {my_list1}")
print(f"my_list2: {my_list2}")




