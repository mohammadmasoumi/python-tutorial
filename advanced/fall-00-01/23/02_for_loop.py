my_list = [1, 2, 3, 4]
my_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = [1, 2, 3, 4]

iterator = iter(my_list)  # iterator

while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    else:
        print(item)

print("---------------------------")
for item in my_list:
    print(f"item: {item}")
    my_list.remove(item)

print("---------------------------")
for item in my_list1:
    print(f"item: {item}")
    my_list1.remove(item)

print("---------------------------")
for item in my_list2:
    print(f"item: {item}")
    my_list2.append(item)
