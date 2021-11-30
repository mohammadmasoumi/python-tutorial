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

#
print(fruits[0])
print(fruits[-5])

#
print(fruits[1])
print(fruits[-4])

#
print(fruits[2])
print(fruits[-3])

#
print(fruits[3])
print(fruits[-2])

#
print(fruits[4])
print(fruits[-1])

print("first", fruits[0])  # first - positive
print("first", fruits[-len(fruits)])  # first - negative

print("last", fruits[len(fruits) - 1])  # last - positive
print("last", fruits[-1])  # last - negative

print(f"len: {len(fruits)}")

print(fruits)
