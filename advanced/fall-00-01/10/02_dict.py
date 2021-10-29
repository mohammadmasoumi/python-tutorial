# define a dict
# key - value pairs

# O(1)
#  hash("ali aliabadi") --> index
# tel_book = [1234 , 1235, 2235]
tel_book = {
    # key: value
    "ali aliabadi": 1234,
    "ali asghar": 1235,
    "asghar agha": 2235,
    # 0: 12367
}

# value = dict[key]
print(tel_book["ali aliabadi"])

# if key does not exist
# KeyError: 0
# print(tel_book[0])
# no index
print(tel_book.get(0))
print(tel_book.get(0, "default value"))

# keys should be hashable
# hash
print(hash(12))
print(hash("ali"))
print(hash("ali aliabadi"))
# print(hash([1, 2])) # TypeError: unhashable type: 'list'
print(hash((1, 2)))
# print(hash([(1, 2)])) # TypeError: unhashable type: 'list'
# print(hash(([1, 2], 2)))  # a list in tuple TypeError: unhashable type: 'list'

empty_dict = {}
dict1 = dict({10: 1, 200: 2, 300: 3, 100000: 0})  # {1:1, 2:2}
dict2 = dict([(1, 2), (2, 3)])  # {1:2 , 2:3}
dict3 = dict(a=2, ali=20, b=3)  # {a:2 , b:3}
dict4 = {1: 2, 2: 3}
dict5 = {"a": 2, "ali": 20, "b": 3}
dict6 = {
    "a": [1, 2, 3, 4],
    "ali": (20, 1),
    "b": 3,
    # 1: 1000,
    True: 1000000,
    False: 1,
    None: 1000  # accepted
}

print(dict4[1])
# print(dict3[a])
print(dict3["a"])
print(dict3["ali"])
print(f"dict6[1]: {dict6[1]}")
print(f"dict6[True]: {dict6[True]}")
# print(f"dict6[2300]: {dict6[2300]}") # KeyError: 2300
print(f"dict6[None]: {dict6[None]}")
print(f"dict6[0]: {dict6[0]}")

# check hash
print(hash(True))
print(hash(1))
print(hash(2300))
print(hash(None))
print(hash(0))
print(hash(False))

# magic function
# class M:
#
#     def __hash__(self):
#         return 2
#
# m = M()
# print(hash(m))
