list1 = [12, 13, 14]
list2 = [12, 14, 15]

set1 = set(list1)
set2 = set(list2)

print(set(list1).difference(set(list2)))
print(set1.difference(set2))
