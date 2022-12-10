# hashing
# built-in function
# hash

set1 = set()

set1.add(True) # hash(True) => 1
set1.add(1) # hash(1) => 1

print(set1) # {True}
print("-------------------------")
print(hash(1))
print("ali", hash("ali"))
print("ali", hash("ali"))
print(hash("ial"))
print(hash(1.1))
print(hash(1.0))
print(hash(True))
print(hash(False))
print(hash((1, 2)))

print("---------------------------")
# hashable and unhashable
# TypeError: unhashable type: 'list'
# print(hash([1, 2]))
# TypeError: unhashable type: 'list'
# print(hash(([1, 2], )))
# TypeError: unhashable type: 'set'
# print(hash({1, 2}))
