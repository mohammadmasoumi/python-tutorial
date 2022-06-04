my_list1 = [1, 2, 3]
my_list2 = [2, 3, 4]


intersection = []

for item1 in my_list1:
    for item2 in my_list2:
        if item1 == item2:
            intersection.append(item1)

print(intersection)

# -----------------------------------
difference = []
for item1 in my_list1:
    for item2 in my_list2:
        if item1 == item2:
            break
    else:
        difference.append(item1)

print(difference)

