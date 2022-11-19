
# "12 13 14"
# int("12 13 14") Wrong
# input().split()
# ["12", "13", "14"]
items1 = list(map(int, input().split()))
items2 = list(map(int, input().split()))

# items1 - items2
difference = []

# items1 ^ items2
intersection = []

for item in items1:

    # is_exist = False
    # for elem in items2:
    #     if item == elem:
    #         intersection.append(item)
    #         is_exist = True
    # if not is_exist:
    #     difference.append(item)

    # elem in list
    # elem not in list
    if item not in items2:
        difference.append(item)
    else:
        intersection.append(item)

print(f"intersection: {intersection}")
print(f"difference: {difference}")

items1_set = set(items1)
items2_set = set(items2)

print(f"intersection: {items1_set.intersection(items2_set)}")
print(f"difference: {items1_set.difference(items2_set)}")
