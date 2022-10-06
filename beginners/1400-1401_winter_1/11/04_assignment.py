# map filter

# "12 13 14"
# [12, 13, 14]
# n = input()

# print(n)

"""
5
ali
hassan
hossein
mohammad
asghar
----------------
3 
ali
mobin
hassan
"""
n = int(input())

# print(n, type(n))
# n: 12, idx: 0 ... 11
my_names = []

for _ in range(n):
    name = input()
    my_names.append(name)
    # my_names.append(input())

print(my_names)




