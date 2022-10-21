# Method on list

my_list = [1, 2, 3, 4]

# insert
#            index item
my_list.insert(0, 5)

print(my_list)

# append
my_list.append(5)

print(my_list)

# [5, 1, 2, 3, 4, 5]
# remove(item)
my_list.remove(5)
# ValueError: list.remove(x): x not in list
# my_list.remove(10)

# del my_list
# remove from the left side
print(my_list)

# pop

item1 = my_list.pop()
item2 = my_list.pop(0)
# IndexError: pop index out of range
# my_list.pop(5)
print(my_list)

"""
[1, 2, 3, 4, 5]

.remove(1)

[1, 3, 4, 5]
.pop(1)
item = .pop(1)
"""
# extend

# TypeError: 'int' object is not iterable
# my_list.extend(12)

#  list.extend() takes exactly one argument (2 given)
# my_list.extend("banana", "orange") # Guess: 

# tuple: (item1, item2)
my_list.extend(("banana", "orange"))

my_list.extend("banana")
my_list.extend(["banana", "orange"])

# append
my_list.append(12)
print(my_list)

# TypeError: list.append() takes exactly one argument (2 given)
# my_list.append(12, 13)

# index(item)
print(my_list.index("orange")) # [4] ? 12

# my_list[5:]
#                                              7
# ['b', 'a', 'n', 'a', 'n', 'a', 'banana', 'orange', 12]
print(my_list[5:].index("orange")) # 4 ? 12

first = my_list.index("orange")
print(first + my_list[first + 1:].index("orange") + 1)

print(my_list.index("orange", 6))
#                           start end
print(my_list.index("orange", 6, 13))
print(my_list.index("orange", 4, 13))

# ValueError: 'orange' is not in list
# print(my_list.index("orange", 13))

# Membership operator

print("a" in my_list)
print("a" not in my_list)

# count
print(my_list.count("a"))
print(my_list.count("asghar")) # 0
my_list.append([1, 2, 3])
print(my_list.count([1, 2, 3]))