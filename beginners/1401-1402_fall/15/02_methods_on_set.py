set1 = {1, 2, 3}
set2 = {1, 2, 4}

# def update(*s: Iterable[_T])
set1.update("mostafa")
set1.update((1, 2))
set1.update([4, 5])
set1.update({5, 6})
# TypeError: 'int' object is not iterable
# set1.update(20)
print(set1)

# Remove an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.
#     set1.remove(10)
# KeyError: 10
# set1.remove(10)
set1.remove(2)
print(set1)

# Remove an element from a set if it is a member.
# If the element is not a member, do nothing.
set1.discard(10)
set1.discard(1)
print(set1)

# Remove and return an arbitrary set element.
# Raises KeyError if the set is empty.
item = set1.pop()
print(item)
print(set1)

# Return a shallow copy of a set.
set1_copy = set1.copy()
print(set1_copy)

# Add an element to a set.
# This has no effect if the element is already present.
set1.add(30)
print(set1)

# Remove all elements from this set.
set1.clear()
print(set1)
