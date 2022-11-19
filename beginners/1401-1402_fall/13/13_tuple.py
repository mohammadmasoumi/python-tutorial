a = [1, 2, 3]
b = [4, 5, 6]

tuple1 = (a, b)
print(tuple1)

a.append(100)
print(tuple1)

"""
    [4, 5, 6, 100]
    |
    |
    |
(a, b)
 |
 |
[1, 2, 3]

"""