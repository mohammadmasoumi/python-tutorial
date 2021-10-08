args = map(int, input().split())
"""
item > max
pre_max = max
max = item
max > item > pre_max
pre_max = item 
"""
max_num = 0

for item in args:
    if item > max_num:
        max_num = item

print(max_num)
