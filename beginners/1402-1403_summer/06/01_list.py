# list

"""
list type:
  - fixed length list
  - dynamic length list

index:
  - positive index: [0: len-1]
  - negative index: [-len:-1]

len()
"""

# brackets
#          -5 -4 -3 -2 -1
#           0  1  2  3  4
my_list1 = [1, 2, 3, 4, 5]
my_list2 = []

# len
print(len(my_list1))

# access via index
print(my_list1[0])  # 1
print(my_list1[-len(my_list1)])  # 1
print(my_list1[len(my_list1)-1])  # 5
print(my_list1[-1])  # 5
print(my_list1[-2])  # 4

# update
#               0          1          2          3           4
fruits = ["watermelon", "apple", "cucumber", "coconut", "pineapple"]

fruits[2] = "orange"
# fruits = ["watermelon", "apple", "orange", "coconut", "pineapple"]

# IndexError: list assignment index out of range
# fruits[10] = "banana"
print(fruits)
# IndexError: list assignment index out of range
# fruits[5] = "tomamto"

# delete

del fruits[2]
print(fruits)
# fruits = ["watermelon", "apple", "coconut", "pineapple"]
(fruits)

# my_list = []
# item = input()
# item2 = input()
# my_list.append(item)
# my_list = [item, item2]
