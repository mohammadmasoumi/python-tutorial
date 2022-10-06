a = {1, 2, 3, 4}

print(f"len: {len(a)}")
print(f"type: {type(a)}")

# no list in set - [1, 2, 3]
# hash

b = {True, False, None, 1, "apple", 20.3, (1, 2)}
print(b)

a1 = 12
g1 = 12.2
b1 = (1, 2, 3)
d1 = (1, 2, 3)
c1 = "hello"
k1 = "Hello"
n1 = True
m1 = 1
l1 = False
o1 = 0
# a2 = [1, 2, 3]
# a3 = (1, [1, 2, 3])

print("------------------------------")
print(f"a1 {hash(a1)}")
print(f"g1 {hash(g1)}")
# 529344067295497451
# 529344067295497451

print(f"b1: {hash(b1)}")
print(f"d1: {hash(d1)}")
print(f"c1: {hash(c1)}")
print(f"k1: {hash(k1)}")
print(f"n1: {hash(n1)}")
print(f"m1: {hash(m1)}")
print(f"l1: {hash(l1)}")
print(f"o1: {hash(o1)}")

# print(hash(a2))
# print(hash(a3)) # typeError: unhashable type: 'list'
