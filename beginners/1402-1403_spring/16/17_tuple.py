tuple1 = (1, True, "hello", [1, 2], 1.0, (1, ))
# TypeError: 'tuple' object does not support item assignment
# tuple1[2] += "asghar"

tuple1 = (1, True, "helloasghar", [1, 2], 1.0, (1, ))
tuple1[3].append(3)

print(tuple1)

print("--------------------------------------")
#           0      1
list1 = [(1, 2), (3, 4)]

print(list1[0], type(list1[0]))
list1.append(5)  # [(1, 2), (3, 4), 5]
print(list1)

# AttributeError: 'tuple' object has no attribute 'append'
# list1[0]: tuple
# list1[0].append(5)  # [(1, 2, 5), (3, 4), 5]
print("--------------------------------------")

tuple1 = ([1, 2], (10, 20))
print(tuple1[0], type(tuple1[0]))
tuple1[0].append(3)
print(tuple1[0], type(tuple1[0]))

for item in tuple1:
    if isinstance(item, list):
        item.append(100)

print(tuple1)

#          variable , type
# isinstance(item, list)
# type(variable) == type
