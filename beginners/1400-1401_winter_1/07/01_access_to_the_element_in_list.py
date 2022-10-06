
# brackets
#            -7         -6        -5          -4      -3          -2         -1
#            0          1         2           3       4           5           6
fruits = ["orange", "banana", "cucumber", "apple", "peach", "watermelon", "coconut"]

# ["orange", "cucumber", "peach", "coconut"]
print(fruits[0:-1:2])
print(fruits[0::2])
print(fruits[::2])

# ["orange", "banana", "apple", "peach"]
print("-------------------------")
print(fruits[:2] + fruits[3:5])
print("-------------------------")
#  ["orange", "cucumber", "apple", "watermelon"]
print(fruits[:3:2] + fruits[3:6:2])
print("-------------------------")
#  ["orange", "watermelon", "apple", "cucumber"]
print(fruits[::5] + fruits[-4:-6: -1])
print("-------------------------")
#  ["orange", "watermelon", "cucumber"]
print(fruits[::5] + fruits[2:3])

# access to the element
print(fruits[2])
print(fruits[-1])

# range index
# [start:end:step]
# [included: not included, step]

print(fruits[1:5:2]) # ["banana", "apple"]
print(fruits[3:3]) # step: 1, []
# range index => list
# access element => one element
print(fruits[3:4], fruits[3]) # fruits[3]

# start: 1 => banana
print(fruits[1:])
# start: -2, step: +1
print(fruits[-2:])
# ['watermelon', 'peach', 'apple', 'cucumber', 'banana', 'orange']
print(fruits[-2::-1])

# ['coconut', 'watermelon', 'peach', 'apple', 'cucumber', 'banana', 'orange']
print(fruits[::-1]) # ?