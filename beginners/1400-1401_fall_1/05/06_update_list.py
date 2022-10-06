fruits = ["apple", "orange", "banana"]
print(fruits)

fruits[0] = "watermelon"
print(fruits)

fruits[2] = "peach"
print(fruits)

# IndexError: list assignment index out of range
# fruits[3] = "cucumber"
# print(fruits)
fruits.append("cucumber")
print(fruits)

print('---------------------------------------------')
fruits = ["apple", "orange", "banana"]
for index, item in enumerate(fruits):
    if item == "apple":
        fruits[index] = "watermelon"

print(fruits)
