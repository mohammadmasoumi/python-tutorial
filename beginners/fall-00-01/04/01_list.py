# list

# variable name
#            0         1        2        3
#           -4        -3      -2        -1
# len: 4
# contains element -> element0 = "orange"
# [0:len-1]
# first index: 0
# last index: len-1
fruits = ["orange", "apple", "peach", "banana"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# ? IndexError: list index out of range
# print(fruits[4])

# the length of list
print(len(fruits))

# ----------------------
# duplicate value allowed
print("-------------------------------------")
list2 = ["ali", "ali", "hossein", "asghar"]
print(list2[0])
print(list2[1])

# ordered
list2 = ["ali", "ali", "hossein", "asghar"]
print(list2[0])
print(list2[1])

# access elements
list3 = ["A", "B", "C", "D", "E", "F"]
print(list3[0])
# [start_index: end_index(not included)]
# [0:2] -> 0, 1
print(list3[0:2])

# [:end_index] -> start_index=0 by default
print(list3[:2])  # [0:2]

# [start_index:] -> end_index=len-1 by default
print(list3[2:])  # [2:6]
print(list3[2:len(list3)])  # [2:6]

# empty
print(list3[0:0])

# negative index

print(list3[-1])
print(list3[-2:])
print(list3[:-2])
print(list3[-5:-2])
