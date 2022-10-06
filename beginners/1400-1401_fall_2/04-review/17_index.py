"""
len: 5

# built-in len(variable_name)
len()



"""
# index: [0, ..., len -1]
# 0, 1, 2, 3, 4

# first index: 0
# last index: len - 1

#            0        1        2          3          4
fruits = ["orange", "banana", "apple", "cucumber", "peach"]

# item access
# variable_name[index]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

print("first", fruits[0])  # first
print("last", fruits[len(fruits) - 1])  # last

print(f"len: {len(fruits)}")

print(fruits)
