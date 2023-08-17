# Review

# ------ mutable
my_list = [1, 2, 3]
my_list.append(5)
"""
                2     5  
                ^     ^
                |     |
my_list --> [*, *, *, *]
             |     |
             v     v
             1     3

COPY
        [*, *, *, *, *]
        [*, *, *, *, *, , , , ,]
"""


my_list = [1, 2, 3, 4, 5]
# ------ immutable
a = 12
b = 12
a = 13
b = 14
"""
[12]

12 GC
a --> 13
14 <-- b
"""


# Shallow copy vs deep copy
