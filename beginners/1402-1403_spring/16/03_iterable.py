# Iterable

"""
Iterable vs Iterator

Iterable: datatype has the ability for for-loop
 - list 
 - str
Iterator: you can loop over it
 - built-in:
        next

"""

my_list = [1, 2, 3, 4, 5]

# TypeError: 'list' object is not an iterator
# print(next(my_list))

# Iterator = iter(Iterable)
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))  # StopIteration

# iterable
for item in my_list:
    print(item)

"""
for loop

iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        yield item
    except StopIteration:
        break
"""
