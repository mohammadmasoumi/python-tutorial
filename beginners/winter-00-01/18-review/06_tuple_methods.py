

my_tuple = (1, 2, 3, 2, 1)

# count(item)
print(my_tuple.count(2))
print(my_tuple.count(10))

# index(item, start, end)
print(my_tuple.index(1))
print(my_tuple.index(1, 1))
# ValueError: tuple.index(x): x not in tuple
print(my_tuple.index(1, 1, 3))