# all elements of set, must be hashable
# immutables are hashable

#   x ->  [hash function] -> int
# set2 = {[1, 2], [3, 4]}

# TypeError: unhashable type: 'list'
# print(set2)

# bultin function
# hash
print(hash(12))
print(hash("ali"))
print(hash("ali"))
print(hash(12.2))

# hash(True) == hash(1)
print(hash(True))
print(hash(1))

# check hash
set3 = {1, True}
print(set3) # 1  

