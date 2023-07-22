a = [1, 2, 3, 4]
b = a

"""
a
|
[1, 2, 3, 4, 5, 6]
|
b
"""

print(f"a: {id(a)}, b: {id(b)}")
print(a == b)
print(a is b)
a.append(5)
b.append(6)

print(f"a: {b}, b: {b}")

print("------- SHALLOW COPY --------")
a = [1, 2, 3, 4]
b = a.copy()

"""
a
|
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 6]
|
b
"""

print(f"a: {id(a)}, b: {id(b)}")
print(a == b)  # True
print(a is b)  # False
a.append(5)
b.append(6)

print(f"a: {a}, b: {b}")
print("------- SHALLOW COPY --------")
a = [[1, 2], 3, 4]
b = a.copy()
#        0  1
# a[0]: [1, 2]
# a[0][0]: 1
# a[0][1]: 2
# a[1]: 3
# a[2]: 4

"""
SHALLOW COPY
a
|
[*, 3, 4]
 |
[1, 2]
 |
[*, 3, 4]
|
b
"""

"""
DEEP COPY
a
|
[*, 3, 4]
 |
[1, 2]
[1, 2]
 |
[*, 3, 4]
|
b
"""

print(f"a: {id(a)}, b: {id(b)}")
print(a == b)  # True
print(a is b)  # False
a[0].append(5)
b[0].append(6)

print(f"a: {a}, b: {b}")
print("------- DEEP COPY --------")
from copy import deepcopy
a = [[1, 2], 3, 4]
b = deepcopy(a)

"""
DEEP COPY
a
|
[*, 3, 4]
 |
[1, 2]
[1, 2]
 |
[*, 3, 4]
|
b
"""

print(f"a: {id(a)}, b: {id(b)}")
print(a == b)  # True
print(a is b)  # False
a[0].append(5)
b[0].append(6)

print(f"a: {a}, b: {b}")