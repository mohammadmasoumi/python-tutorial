my_list = [1, 2, 3, 4, 5, 6]

odd_list = []

for item in my_list:
    # if item % 2 == 1:
    # bool(item % 2)
    # even: not item % 2 | item % 2 == 0
    if item % 2:
        odd_list.append(item)

print(odd_list)

# list comprehension

#     [true] if [condition] else [false]
name = "mina" if 2 else "baran"

# my_list = [1, 2, 3, 4, 5, 6]
# doubled
print([item * 2 for item in my_list])
print([item // 2 for item in my_list])

# my_list = [1, 2, 3, 4, 5, 6]
# only odds
# [[final_item] for [item] in [list] if [condition]]
print([item for item in my_list if item % 2])
print([item * 2 for item in my_list if item % 2])

# my_list = [1, 2, 3, 4, 5, 6]
# [[true] if [condition] else [false] for [item] in [list]]
print([item * 2 if item % 2 else item // 2 for item in my_list])

# fallten list
# my_list = [[1, 2, 3], [4, 5, 6]]
# my_list = [1, 2, 3, 4, 5, 6]
my_list = [[1, 2, 3], [4, 5, 6]]
# items: [1, 2, 3]
# items: [4, 5, 6]
print([item for items in my_list for item in items])
print([item for items in my_list for item in items if not item % 2])
print([item // 2 if not item % 2 else item *
      2 for items in my_list for item in items])
