t1 = (1, [1, 2], [3, 4])

t1[1].append(3)
print(t1)

# TypeError: 'tuple' object does not support item assignment
# t1[1] = [1, 2, 3, 4]

"""
t1

 2
 |
 X  [1, 2, 3]
 |  |
(*, *, *)
 |     |
 1     [3, 4]

# Change tuple XXX
t1[0] = 2 X 
t1[1] = [1, 2, 3, 4] X

"""

t2 = (1, ([1, 2], 3), [3, 4])
t2[1][0].append(3) # tuple
print(t2)