# hash
# datatype and all items included must be immutable

print(hash(1))
print(hash(2))
print(hash(2.1))
print(hash(-1))
print(hash(-2))
print(hash(-3))
print(hash("ali"))
print(hash(True))
print(hash(False))
# -------------
print(hash((1, 2, 3)))
# unhashable
# TypeError: unhashable type: 'list'
# (1, 2, [1, 2, 3])
# print(hash((1, 2, [1, 2, 3])))
# TypeError: unhashable type: 'list'
# print(hash([1, 2, [1, 2, 3]]))
# TypeError: unhashable type: 'set'
# print(hash({1, 2, 3}))

"""
(1, 2, [1, 2, 3])

(*, *, *)
 |  |  |
 v  v  v
 1  2  [1, 2, 3]

value = (1, 2, [1, 2, 3])  
hash(value) -> 1234

value[2].append(4)
# (1, 2, [1, 2, 3, 4]) 
hash(value) -> 1235
"""
