"""
a
b

max(a, b)

input
12
13

output
13
"""

a = int(input())
b = int(input())

"""
# 1
a = 13
b = 12

13

# 2
a = 12
b = 13

13
"""

if a >= b:
    print(a)
else:
    print(b)
