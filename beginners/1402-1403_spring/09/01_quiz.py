my_list = [[10, 20], [30, 40, 50]]

# my_list = [[10, 20], [30, 50. 40], 10, 20, 30]
# my_list = [[10, 21], [30, 51, 40], 11, 21, 31]

"""
1. for loop [X]
2. max item [X]
3. calculate target value

immutable -> idx
mutable -> no index is needed

immutable: 
    int
    str
    float
    bool

mutable:
    list
"""

for items in my_list:
    # item: list [10, 20]
    items.append(max(items) + 1)

print(my_list)
