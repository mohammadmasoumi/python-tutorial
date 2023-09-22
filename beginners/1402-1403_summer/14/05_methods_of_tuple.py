#     0  1  2  3
t1 = (1, 1, 2, 3)

# Return number of occurrences of value.
print(t1.count(1))

# Return first index of value.
# Raises ValueError if the value is not present.
print(t1.index(1))
#            value start stop  
print(t1.index(1, 1, 4))

# ValueError: tuple.index(x): x not in tuple
# print(t1.index(1, 2, 4))