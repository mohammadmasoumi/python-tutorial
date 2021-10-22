set1 = {1, 2, 3}
set2 = {40, 2, 3}
set1.add(3)
set1.add(4)

print(set1)

set1.update((1, 2, 3, 10))
print(set1)
set1.update([1, 2, 3, 11])
print(set1)
set1.update(set2)
print(set1)
# {1, 2, 3, 4, 40, 10, 11}


# def func1(s1):
#     s1.add(3)
#     return None
#
# def fund1(s1):
#     s1.add()
#     return s1
