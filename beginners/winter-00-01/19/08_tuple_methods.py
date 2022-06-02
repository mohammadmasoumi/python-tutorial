my_tuple = (1, 2, 3, 4, 5 ,6, 1, 2)

# index
#              elem, start, stop
#                 value -> index
print(my_tuple.index(1))
#                     value in (start: stop)
print(my_tuple.index(1, 2))

# ValueError: tuple.index(x): x not in tuple
# print(my_tuple.index(10, 2))

# count
print(my_tuple.count(1))
print(my_tuple.count(10))

