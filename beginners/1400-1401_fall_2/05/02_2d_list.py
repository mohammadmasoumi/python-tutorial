list6 = [[1, 2, 3], [4, 5, 6]]

"""
[
[1, 2, 3], 
[4, 5, 6]
]
"""

"""
      0                     1
   0  1  2              0  1  2  
[ [1, 2, 3],           [4, 5, 6]      ]

"""
print(list6)

# list1 = [1, 2, 3]
list1 = list6[0]

#  0  1  2
# [1, 2, 3]
print(list1)
print(type(list1))
print(list1[0])
print(list1[1])
print(list1[2])

# -----------------

# print(list1[0])
print(list6[0])  # [1, 2, 3]
print(list6[0][0])  # 1

print("---------------------")
# -----------------
# [[1, 2, 3], [4, 5, 6]]

list2 = list6[1]
print(list6[0][0])
print(list6[1][0])
print(list6[1][2])
print(list6[1][1])
print(list6[0][1])

# IndexError: list index out of range
# print(list6[0][3])
# print(list6[2][1])
