# question?

d = {'a': 1}
my_list = [d for _ in range(4)]
my_list[0].update(b=2)
print(my_list)
print(id(my_list[0]), id(my_list[1]), id(my_list[2]), id(my_list[3]))

"""
Reference

[*, *, *, *]
 |  |  |  |
 V  V  V  V
 {'a': 1, 'b': 2}

"""

print("------------")
# each time, create a new dict
my_list = [{'a': 1} for _ in range(4)]
my_list[0].update(b=2)
print(my_list)
print(id(my_list[0]), id(my_list[1]), id(my_list[2]), id(my_list[3]))

"""
{'a': 1}     {'a': 1}
    ^        ^
    |        |
[*, *,    *, *]
|         |  
V         V  
{'a': 1} {'a': 1}
"""