"""
len: 5

# built-in len(variable_name)
len()



"""
# index: [0, ..., len -1]
# 0, 1, 2, 3, 4

# first index: 0
# last index: len - 1

#             0                                     len -1
#          -len                                      -1
#            0        1        2          3           4
#           -5       -4       -3         -2          -1
fruits = ["orange", "banana", "apple", "cucumber", "peach"]

# item access
# variable_name[index]

# access to single element
print(fruits[0])
print(fruits[-5])
print("-------------------------")
# range index
"""
                included    not included
variable_name[start index: end index: step]

[start, end)

"""

# 1, 2, 3
# [start, end, step]
# [1: 4: +1(default)]
# "banana", "apple", "cucumber"
print(fruits[1:4])

# [start:]
# [start: len(default): 1(default)]
# [1: 4: +1]
# "banana", "apple", "cucumber", "peach"
print(fruits[1:])

# [:end]
# [0(default): end: 1(default)]
print(fruits[:3])

# [start:end: step]
# [0: 4: 2]


print(fruits[3:3])  # check whether start index is equal to end index

# print(fruits[1: 4: 2])
print(fruits[1: 4: 2])

# ["orange". "cucumber"]
print(fruits[0:4:3])

# [start(default (0)), end(default (len)), 3]
print(fruits[::3])
