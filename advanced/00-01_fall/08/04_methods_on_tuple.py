a_tuple = (10, 1, 1, 2, 3, 4, 5)

# print(a_tuple.count(1))
print(a_tuple.count(20))  # no error
# print(a_tuple.index(1))

# اکر ایتم را پیدا نکند خطای زیر را میدهد.
# ValueError: tuple.index(x): x not in tuple
# index(search_for, from_index)
# print(a_tuple.index(20)) # ValueError: tuple.index(x): x not in tuple
print(a_tuple.index(1))
print(a_tuple.index(1, 2))
print(a_tuple.index(1, 4))

# ValueError: tuple.index(x): x not in tuple
# print(a_tuple.index(2, 3))
