#            0         1        2         3          4
#          [-5]       [-4]     [-3]      [-2]       [-1]       0 1 2 3
fruits = ["orange", "banana", "apple", "cucumber", "peach"]

# range index

"""
list_name[start_index(included): end_index(not included): 1]
list_name[start_index(included): end_index(not included): step]
list_name[start: end: step]
"""

"""
[], ["orange"], ["banana"], ...
"""

# return an element
print(fruits[-4:4])
print(fruits[-5:2])
print(fruits[-4:2])

print(fruits[3])
print(fruits[3:3])  # empty
print(fruits[3:-2])
print(fruits[-2:2])  # empty
print(fruits[-2:0])  # empty
print(fruits[-2:-1])

print(fruits[0])
print(fruits[-5])
print(fruits[1:: 2])
print(fruits[1:: 3])
print(fruits[:: 4])

index = 3
print(fruits[:2] + fruits[3:])
print(fruits[:index], fruits[index:])

print("-------------------------")
# return a list
print(fruits[3: 1: -1])
print(fruits[1:])
print(fruits[-4:])
print(fruits[-1: -4: -1])
print(fruits[:: -1])
print(fruits[:: -2])  # ['peach', 'apple', 'orange']
print(fruits[:: 2])  # ['orange', 'apple', 'peach']
