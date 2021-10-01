fruits = ["orange", "apple", "peach", "banana"]

# append
# add a new element at the end of the list
fruits.append("grape")
# TypeError: append() takes exactly one argument (2 given)
# fruits.append("grape", "asghar")
print(fruits, len(fruits))

# fruits.extend(["banana2", "apple2", "orange2"])
# fruits.append(["banana2", "apple2", "orange2"])

# IndexError: list assignment index out of range
# fruits[5] = "cherry"

# insert at specific index
fruits.insert(3, "cherry")
print(fruits, len(fruits))

# extend
fruit1 = ["orange", "grape"]
fruit2 = ["apple", "banana"]
#
# fruit1.extend(fruit2)
# print(fruit1)
# print(fruit2)

fruit1.append(fruit2)
print(fruit1)
print(fruit1[2])

# remove from the end
print("-------------------------------")
print(fruits)
fruits.pop()
a = fruits.pop()
print(a)
print(fruits)

# count
print("-------------------------------")
print(fruits)
fruits.append("apple")
print(fruits)
print(fruits.count("apple"))
print(fruits.count("orange"))

# index
print("-------------------------------")
print(fruits)
print(fruits.index("apple"))
print(fruits.index("apple", 2))
print(fruits.index("apple", 3))

# remove
print("-------------------------------")
print(fruits)
fruits.remove("apple")
print(fruits)

# clear
# fruits.clear()

#
print(fruits)
# descending
fruits.sort(reverse=True)
# print(fruits.sort()) # return None
print(fruits)

# ascending
fruits.sort()
print(fruits)

# reverse the array
# fruits.reverse()
# print(fruits)

# fruits.copy()
