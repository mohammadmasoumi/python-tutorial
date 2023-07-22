# slicing
# list[start:end:step]
# start: included بازه بسته
# end: not included بازه باز
# [2, 6)
# 2, 3, 4, 5
# [2, 6) step: 2
# 2, 4
# [6, 2) step: -2
# 6, 4
# [4, 6) step: -1
# 
# 
#         -7 -6 -5 -4 -3 -2 -1
#          0  1  2  3  4  5  6
my_list = [1, 2, 3, 4, 5, 6, 7]

# positive step: 1 move forward|move right
# negative step: -1 move backward|move left
print(my_list[2])
print(my_list[2:5]) # step: 1, [3, 4, 5]
print(my_list[4:2]) # step: 1, [] always return list
print(my_list[4:2:-1]) # step: -1. [5, 4]
print(my_list[4:-1:-1]) # step: -1, []
print(my_list[4:-1:1]) # step: 1, [5, 6]

#         -7 -6 -5 -4 -3 -2 -1
#          0  1  2  3  4  5  6
my_list = [1, 2, 3, 4, 5, 6, 7]

print(my_list[2:]) # [3, 4, 5, 6, 7]
print(my_list[2::-1]) # [3, 2, 1]
print(my_list[:2:-1]) # [7, 6, 5, 4]
print(my_list[:2:1]) # [1, 2]

# 
print(my_list[::-2]) # [6, 4, 2], [7, 5, 3, 1]
print(my_list[::-1]) # reverse [7, 6, 5, 4, 3, 2, 1] 
print(my_list[2: 5: 2]) # [3, 5]
print(my_list[0: -2: 3]) # [1, 4]

# example
#                   -8         -7         -6       -5      -4         -3          -2        -1
#                   0          1          2         3        4          5           6        7
asghar_fruits = ["orange", "banana", "cucumber", "apple", "lemon", "watermelon", "melon", "peach"]

# ["orange", "cucumber"]
print(asghar_fruits[0:3:2])
# ["orange", "cucumber", "lemon", "melon"]
print(asghar_fruits[::2])
print(asghar_fruits[0:7:2])
print(asghar_fruits[-8:-1:2])
# ["watermelon", "apple", "banana"]
print(asghar_fruits[5::-2])
print(asghar_fruits[5:0:-2])
# ["peach", "melon", "watermelon", "lemon", "apple", "cucumber"]
print(asghar_fruits[7:1:-1])
print(asghar_fruits[-1:-6:-1])
# ["peach", "lemon", "banana"]
print(asghar_fruits[7::-3])
print(asghar_fruits[7:0:-3])
# ["banana", "apple", "watermelon"]
print(asghar_fruits[1:6:2])
# ["peach", "melon", "banana", "orange"]
print(asghar_fruits[7:5:-1] + asghar_fruits[1::-1])
print(asghar_fruits[7:5:-1] + asghar_fruits[0:2:1]) # X WRONG
# ["apple", "peach", "melon", "lemon", "cucumber"]
print(asghar_fruits[3::4] + asghar_fruits[6:1:-2])

# WRONG
#           "orange"  + []
print(asghar_fruits[3] + asghar_fruits[2:])