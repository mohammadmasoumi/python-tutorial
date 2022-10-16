my_set1 = {1, 2}
my_set2 = {1, 2, 3}
my_set3 = {3, 4}

print(my_set1.issubset(my_set2))
print(my_set1.issuperset(my_set2))
print(my_set2.issuperset(my_set1))
print(my_set1.isdisjoint(my_set3))
print(my_set2.isdisjoint(my_set3))
