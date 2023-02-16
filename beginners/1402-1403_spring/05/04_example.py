# brackets
#            -7         -6        -5          -4      -3          -2         -1
#            0          1         2           3       4           5           6
fruits = ["orange", "banana", "cucumber", "apple", "peach", "watermelon", "coconut"]
#  ["orange", "cucumber", "peach"]
print(fruits[0:-1:2])
#  ["orange", "cucumber", "peach",  "coconut"]
print(fruits[0::2])
#  ["orange", "cucumber", "peach",  "coconut"]
print(fruits[::2])
# ['orange', 'banana', 'apple', 'peach']
print(fruits[:2] + fruits[3:5])
print(fruits[:3:2] + fruits[3:6:2])
print(fruits[::5] + fruits[-4:-6: -1])
# print(fruits[::5] + fruits[2:3])
# print(fruits[2])
# print(fruits[-1])
# print(fruits[1:5:2])
# print(fruits[3:3])
# print(fruits[3:4], fruits[3])
# print(fruits[1:])
# print(fruits[-2:])
# print(fruits[-2:: -1])
# print(fruits[:: -1])
