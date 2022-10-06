fruits = ["orange", "banana", "apricot", "cucumber", "watermelon", "orange"]
# fruits = [ "banana", "apricot", "cucumber", "watermelon", "orange"]

"""
if variable type is list
variable_name(.)(method_name)
"""

# 1
# Number of occurrences of value.
print(fruits.count('orange'))
# print(fruits.count('melon'))  # 0

# 2
# all fruits
# print(fruits)
# print(fruits[:])
print(fruits[::2])
# print(fruits[:1])  # ['orange']
# print(fruits[1:])  # ['banana', 'apricot', 'cucumber', 'watermelon', 'orange']
# print(fruits[1:][::3])
# print(fruits[:1] + fruits[1:][::3])
print(fruits[:1] + fruits[1::3])

#      -6        -5        -4         -3           -2         -1
#      0         1         2          3            4           5
#      *                   *          *                        *
# ["orange", "banana", "apricot", "cucumber", "watermelon", "orange"]

# print(fruits)
# 6
print("---------------------------")
print(fruits[-2:][::-1])
print(fruits[len(fruits) - 1:3: -1])
print(fruits[-1: -3: -1])
print("---------------------------")
print(fruits[1:3][::-1])
print(fruits[2:0: -1])
print(fruits[-4:-6: -1])
print(fruits[-1: -3: -1] + fruits[2:0: -1])
print("---------------------------")

# 7
print(fruits[-5::-1] + fruits[3:1: -1] + fruits[0:1])
print(fruits[-5::-1] + fruits[3:1: -1] + fruits[-1:])
print(fruits[-5::-1] + fruits[3:1: -1] + [fruits[-1]])
