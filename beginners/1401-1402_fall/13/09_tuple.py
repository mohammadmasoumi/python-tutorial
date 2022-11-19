list1 = [1, 2, 3]
# immutable
tuple1 = (1, 1, 2, 3)

print(type(list1))
print(type(tuple1))

# iterable
for item in tuple1:
    print(item)

for item in tuple1:
    print(item)

# range(4)
# 0, 1, 2, 3
for index in range(len(tuple1)):
    print(tuple1[index])

# range(4)
# 0, 1, 2, 3
for index, item in enumerate(tuple1):
    print(index, item)


# method
print(tuple1.count(1))
#               value, start, end
print(tuple1.index(1))
print(tuple1.index(2))
print(tuple1.index(1, 1, 4))