my_set = set()

# add
my_set.add(True)  # hash(True) -> 1
my_set.add(1)  # hash(1) -> 1
# my_set: {True} dropped 1
my_set.add(2)
# my_set: {True, 2}
my_set.add(False)
# my_set: {True, 2, False}
my_set.add(0)

print(my_set)  # {1, 2, False} | {True, 2, False}

# discard
"""
(method) discard(__element: Any, /) -> None
Remove an element from a set if it is a member.

Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
"""
my_set.discard(10)
print(my_set)

# remove
"""
(method) remove(__element: Any, /) -> None
Remove an element from a set; it must be a member.

If the element is not a member, raise a KeyError.
"""
# KeyError: 10
# my_set.remove(10)

print("-----------------")
#
my_set = {1, 2, 5}
my_set.update({1, 2, 3, 4})  # iterable
my_set.update([1, 2, 3, 4])
my_set.update((1, 2, 3, 4))
print(my_set)

# example
my_set = set()
my_set.add("ali")
my_set.add("asghar")
my_set.add(False)
my_set.add(True)  # hash(True) -> 1
my_set.add(1)  # hash(1) X drop
my_set.add("funzy")
print(my_set)  # {"ali", "asghar", False, True, "funzy"}

my_set.discard("akbar")
# my_set.remove("akbar") raise exception
my_set.discard("funzy")
print(my_set)

# pop
my_set = set()
my_set.update({1, 2, 3, 4, "ali", True, False})
print(my_set)
# KeyError: 'pop from an empty set'
item1 = my_set.pop()  # remove a random item
print(item1)
item2 = my_set.pop()
print(item2)
