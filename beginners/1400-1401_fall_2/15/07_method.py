a_tuple = (1, 1, 2, 3, 1, 1, 4, 5, 1, 1)

# ctrl + click => definition
# Return number of occurrences of value.
print(a_tuple.count(1))
print(a_tuple.index(1))

# if item does not exist, raise exception
# print(a_tuple.index(12)) # ValueError: tuple.index(x): x not in tuple
#               item, start, end
print(a_tuple.index(1, 3, 10))
