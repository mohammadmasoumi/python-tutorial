"""
4
ali 20 12 19
hassan 20 19 18
mohammad 20 20 20
sina 10 10 10
"""

n = int(input())

# n: 3
# 0, 1, 2
# _

"""
   name avg
[["ali", 19], []]
"""
students = []
for _ in range(n):
    # ["ali", "20", "12", "19"]
    items = input().split()
    name = items[0]
    scores = items[1:]

name = input()
# search name