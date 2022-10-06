"""
data types

int
float
str
bool
list
"""

#        int int int
list1 = [12, 13, 14]

#         str  str  str
list2 = ["a", "b", "c"]

cucumber = "a"
banana = "b"

list3 = [cucumber, banana]
list4 = ["cucumber", "banana"]
list5 = ["cucumber, banana, peach"]  # one element

print(list5[0])

# positive index: 0, ... ,  len - 1
# negative index: -1, ..., -len

#         -5  -4    -3  -2        -1
#         0    1    2    3         4             5
list6 = [True, 12, "a", 12.4, [12, 23, 43]]

print(len(list6))  # 5
print(list6[4])

# IndexError: list index out of range
# print(list6[5])
print(list6[-len(list6)])
