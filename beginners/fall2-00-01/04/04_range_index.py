#             0         1        2         3          4
fruits = ["orange", "banana", "apple", "cucumber", "peach"]

# range index

print(fruits[1], fruits[2], fruits[3])

"""

list_name[start_index(included): end_index(not included): 1]
list_name[start_index(included): end_index(not included): step]
"""

# sub list
print(fruits)
print(fruits[1:3])
print(fruits[0:3] + fruits[4: 5])

# if last index is greater that length of list - it consider whole list
print(fruits[1:10])

# [1: 5(not included)] -> 1, 2, 3, 4
print(fruits[1:5])  # len(fruits): 5
print(fruits[1:len(fruits)])  # len(fruits): 5
