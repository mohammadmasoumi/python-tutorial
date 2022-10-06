my_list = ["apple", "orange", "banana"]
print(my_list)

for item in my_list:
    if item == "apple":
        item = "peach"

for idx, item in enumerate(my_list):
    if item == "apple":
        my_list[idx] = "peach"

counter = 0
for item in my_list:

    print(item)
    counter += 1

print(my_list)

print("--------------------------")
my_list2 = [[1, 2], [3, 4], [5, 6]]
for item in my_list2:
    item.append(10)

print(my_list2)



print("--------------------------")
# start 0, end 12(not included) , step1

# start=0, end=12, step=1
range(12)

# start=0, end=12, step=1
range(0, 12)

# start=12, end=0, step=-1
range(12, 0, -1)

# for item in range(12, 2, -1):
#     print(item)

# unpacking
a, b = [1, 2]
print(a, b)

# ValueError: too many values to unpack (expected 2)
# a, b = [1, 2, 3]

a, *b = [1, 2, 3]
print(a, b)

a, *b, c = [1, 2, 3, 4]
print(a, b, c)

# packing
a, *b, c = range(10)
print(a, b, c)

# a1, b1, c1 = *my_list
print(*my_list)
a2, b2, c2 = my_list
print(*my_list)

# SyntaxError: two starred expressions in assignment
# a, *b, *c = [1, 2, 3, 4]
# print(a, b, c)

# for idx, item in enumerate(my_list):
#     print(idx, item)


# they are the same
for fruit in enumerate(my_list):
    idx, item = fruit
    print(idx, item, fruit)

for idx, item in enumerate(my_list):
    # idx, item = fruit
    print(idx, item)
