# Bitwise operator

"""
and & 
or | 
xor ^ 
not ~!
"""

"""
-------- [and bitwise] min

5 = (101)
7 = (111)

101
111 &
___
101 => (5)

-------- [or bitwise] max

5 = (101)
7 = (111)

101
111 |
___
111 => (7)

-------- [xor bitwise] diff

5 = (101)
7 = (111)

101
111 ^
___
010 => (2)

"""
a = 5
b = 7

print(a & b)
print(a | b)
print(a ^ b)