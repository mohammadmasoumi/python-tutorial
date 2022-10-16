#             -6      -5         -4       -3          -2           -1
#             0        1         2         3          4            5
fruits = ["orange", "apple", "banana", "apricot", "cucumber", "watermelon"]

# ["orange", "banana", "watermelon", "cucumber"]
print(fruits[:3:2] + fruits[:-3:-1] )

# ["orange", "banana", "cucumber"]
print(fruits[::2])

# ["watermelon", "apricot", "apple"]
print(fruits[::-2])

print(fruits[::-1]) # reverse
print(fruits[-5::-1])

print(fruits[2:5])
print(fruits[2:5][1:3][:1][:10])