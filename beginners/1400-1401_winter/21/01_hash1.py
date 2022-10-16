# build-in function
# Hash function
    # 1. one 2 one
    # 2. one direction

# id, hash, int, float, str, type, print, ... 
# keyword: def, if, else, elif, for, while, ...

# hash function
# int -> int

# 2757152818962362128
# 2757152818962362128
print(hash("ali"))
print(hash(12))
print(hash("12"))
print(hash("ali"))
print(hash((1, 2)))
print(hash((1, 2, (3, 4))))
print(hash(12.2))
print(hash(1))
print(hash(True))
print(hash(0))
print(hash(False))

# Invalid sets
# {{1, 2}, 3}
# {[1, 2], 3}
# {([1, 2], 3)}
set1 = set()
set2 = {1, 2}
set3 = set()

# does not change the key
set1.add(True)
set1.add(1)
print(set1)

set2.add(1)
set2.add(True)
print(set2)


# set1.add(hash(12.2))
# print(set1)

# TypeError: unhashable type: 'list'
# set1.add([1, 2])
# TypeError: unhashable type: 'set'
# set1.add(set2)

# TypeError: unhashable type: 'set'
# print(hash({1, 2, 3}))
# TypeError: unhashable type: 'list'
# print(hash(["ali"]))
# TypeError: unhashable type: 'list'
# print(hash((1, 2, [1, 2])))