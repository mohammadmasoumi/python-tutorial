# hash


# built-in hash

# hashable
# immutable(s) are hashable.

# dict, list, set => is not hashable


"""
hash()

khuriju = hash(vorodi)

12 = hash(12)
1258/2346678798 = hash("ali")

un-hashable
hash([1, 2, 3])
hash({1, 2, 3})

"""

a = 12
b = "asghar"
c = 12.3

d1 = (1, 2)  # hashable
d2 = (11.1, 2.1)  # hashable
d3 = ("ali", "karimi")  # hashable
d4 = (True, False)  # hashable
d6 = 10000000000000000000000000000000

# ypeError: unhashable type: 'set'
# d7 = {1, 2, 3}

# TypeError: unhashable type: 'list'
# d5 = ([1, 2], 1)  # un-hashable

# TypeError: unhashable type: 'list'
# d = [1, 2, False]

f = False
f1 = 0
g = True
g1 = 1

# duplicate - ctrl + d
# int(), float(), map(), bool(), enumerate(), str(), list(), tuple(), set(), dict(),

ali = "ali"
print(hash("ali"))
print(hash("ali"))
print(hash(ali))

print(f"{a}: {hash(a)}")
print(f"{a}: {hash(a)}")
print(f"{b}: {hash(b)}")
print(f"{c}: {hash(c)}")
# print(f"d: {hash(d)}")
print(f"{d1}: {hash(d1)}")
print(f"{d2}: {hash(d2)}")
print(f"{d3}: {hash(d3)}")
print(f"{d4}: {hash(d4)}")
# print(f"{d5}: {hash(d5)}")
print(f"{d6}: {hash(d6)}")
# print(f"{d7}: {hash(d7)}")

print(f"{f}: {hash(f)}")
print(f"{f1}: {hash(f1)}")
print(f"{g}: {hash(g)}")
print(f"{g1}: {hash(g1)}")
