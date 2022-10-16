my_list = [1, 2, 3, 4]

"""
1. list-comprehension
[ item * 2 for item in my_list]
[ item for item in my_list]
[ item + 2 for item in my_list]

2. list-comprehension-if
[ item * 2 (for) item (in) my_list (if) item % 2]
[ item for item in my_list if item % 2]
[ item + 2 for item in my_list if item % 2]

3. list-comprehension-if
[ [item * 2] (if) item % 2 (else) [item // 2] (for) item (in) my_list]
"""

print(list(map(lambda value: value*2, my_list )))
print([item * 2 for item in my_list])
print([ item for item in my_list])
print([ item + 2 for item in my_list])

print("-------------------------------------------------")
print([ item * 2 for item in my_list if item % 2])
print([ item + 2 for item in my_list if item % 2])
# map filter
print(list(map( lambda value: value * 2, filter(lambda value: value % 2, my_list)  )))
print("-------------------------------------------------")
# [1, 2, 3, 4]
print([ item * 2 if item % 2 else item // 2 for item in my_list])

print("-------------------------------------------------")

"""
4. list-comprehension-for
[ [item * 2] (if) item % 2 (else) [item // 2] (for) item (in) my_list]

"""
my_list = [  
    [1, 2], 
    [3, 4]
]

# flat
print(my_list)
print([   item  * 2          for items in my_list        for item in items])
print([   item  * 2          for items in my_list        for item in items      if item % 2])
print([   item  * 2  if item % 2 else item // 2        for items in my_list        for item in items ])

# for items in my_list:
#     # items:  [1, 2]
#     # items:  [3, 4]
#     # print(items)
#     for item in items:
#         # items: [1, 2]
#         # item: 1, 2
#         print(item)