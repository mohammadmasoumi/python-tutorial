# without copy
a = [12, 13]
b = a

"""
a -> [12][13]  <- b

b.append(14)
a -> [12][13][14]  <- b

"""

a.append(14)

print(a)
print(b)

print("------------------------")

# shallow
a = [12, 13]
b = a.copy()

"""
a -> [12][13]  <- b

b.append(14)
a -> [12][13][14]
b -> [12][13]

a = [[12, 13]]
b = a.copy()

b -> [0]
      |
    [12][13]
      ^
      |
a -> [0]

a[0].append(14)
print(a) # [[12, 13, 14]]
print(b) # [[12, 13, 14]]


******* DEEP COPY *******

    [12][13]
      ^
      |
a -> [0]


    [12][13]
      ^
      |
b -> [0]

"""

a.append(14)

print(a)
print(b)

print("------------------------")

# shallow
a = [12, 13]
b = a.copy()

"""
a -> [12][13]  <- b

b.append(14)
a -> [12][13][14]
b -> [12][13]
"""

a.append(14)

print(a)
print(b)


# deep copy
from copy import deepcopy

a = [[12, 13]]
b = deepcopy(a)

a[0].append(14)

print(a)
print(b)