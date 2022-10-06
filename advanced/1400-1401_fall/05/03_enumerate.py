# index
"""
counter = 0
for fruit in a_list:
    print(fruit)
    fruit = fruit + "Hello"
    a_list[counter] = fruit
    counter += 1
"""

a_list = ["apple", "orange", "peach"]

# for idx, item in enumerate(a_list):
#     print(idx, item)
#     a_list[idx] = item + "-Hello"
#
# print(a_list)

"""
(0, 'apple-Hello')
(1, 'orange-Hello')
(2, 'peach-Hello')
"""
item = [0, 'apple']
print(item[0])
print(item[1])

for item in enumerate(a_list):
    print(item, item[0], item[1])

# equavalent
# a_list2 = []
# for idx in range(len(a_list)):
#     a_list2.append([idx, a_list[idx]])
#
# print(a_list2)
