fruits = ["orange", "watermelon", "coconut"]

# remove - just working with elemnet
# accept duplicated item
# fruits.append("coconut")
# fruits.insert(1, "coconut")
# print(fruits)

# fruits.remove("coconut")
# print(fruits)
# fruits.remove("coconut")
# print(fruits)
# fruits.remove("coconut")
# a = fruits.remove("coconut")

# ValueError: list.remove(x): x not in list
# fruits.remove("coconut")
print(fruits)

# pop - just working with indexes
# print(fruits.pop())
# 
# fruits.pop(index), default: last element
# fruits.pop()  default: last element
# 
fruit = fruits.pop(1)
# IndexError: pop index out of range
# fruits.pop(10)
fruits.pop()
#  pop from empty list
# fruits.pop()

print(fruit)
print(fruits)
