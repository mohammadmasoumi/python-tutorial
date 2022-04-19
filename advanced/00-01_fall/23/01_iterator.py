"""
list
tuple
dict
str

collection
sequence
iterator
"""

my_list = [1, 2, 3]  # iterable

my_iterator = iter(my_list)  # iterator

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())

# range
# یک بار مصرف نیست
# my_range = range(10)
#
# for item in my_range:
#     print(item)
#
# for item in my_range:
#     print(item)

# map
# یک بار مصرف
my_map = map(str, [1, 2, 3])
print(my_map)
print(my_map)

print("-----------------")
for item in my_map:
    print(item)

print("-----------------")
for item in my_map:
    print(item)

# exhausted
# disposal

# print(next(my_iterator)) # StopIteration
# print(next(my_iterator))
