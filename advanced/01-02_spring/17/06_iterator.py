"""
list 
tuple
set
dict

iterable
sequence
iterator
"""

my_list = [1, 2, 3, 4]

iterator = iter(my_list)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# dunder method
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# StopIteration
# print(next(iterator))

my_map = map(int, my_list)

print("----------------------")
for item in my_map:
    print(item)


print("----------------------")
for item in my_map:
    print(item)


# disposal
# exhausted
