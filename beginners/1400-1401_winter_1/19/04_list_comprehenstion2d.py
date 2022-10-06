my_list = [[1, 2], [3, 4]]
# [1, 2, 3, 4]

# [
#   [1, 2], 
#   [3, 4]
# ]
# items: [1, 2] - item: 1, item: 2
# [item * 2 (for items in my_list) (for item in items)]
# flat
print([item * 2 for items in my_list for item in items])
print([item * 2 if item % 2 else item // 2 for items in my_list for item in items])

new_my_list = []
for items in my_list:
    for item in items:
        new_my_list.append(item * 2)
