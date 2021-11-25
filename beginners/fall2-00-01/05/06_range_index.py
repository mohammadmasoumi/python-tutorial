# len(fruits): 4
#            -4         -3         -2       -1
#            0          1          2        3
fruits = ["banana", "cucumber", "apple", "orange"]

# print(fruits[0])
# print(fruits[-4])
# print(fruits[-len(fruits)])
# print(fruits[-1])

#                  4
#                  4    -  1
#                  3
# print(fruits[len(fruits) - 1])

"""
  
[start(included): end(not included): step(default=1)]
[start: end)

"""
#      -4         -3         -2       -1
#      0          1          2        3
# ["banana", "cucumber", "apple", "orange"]

# 1
print(fruits[0: 3])
print(fruits[0: 3: 2])

# 2
print(fruits[-4: -1])
print(fruits[-1: -4: -1])
print(fruits[-1: -4])  # [NOTE]
print(fruits[3: 3])  # [NOTE] empty
