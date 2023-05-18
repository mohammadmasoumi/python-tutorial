# Set
"""
1. Mutable
2. Unordered -> no index
3. Duplication is not allowed
4. Hashable element
"""
my_set = set()

# list, tuple, str -> iterable 

# Add
my_set.add(1)

print(my_set)

# Update
            # iterable
my_set.update([1, 2, 3])
print(my_set)

            # iterable
my_set.update((1, 2, 3, 4))
print(my_set)

            # iterable
my_set.update("salmanpour")
print(my_set)

            # iterable
my_set.update((11, 2, 3, 4))
print(my_set)

my_set.add("salmanpour")
print(my_set)

# my_set.add("salmanpour", 12)
# TypeError: set.add() takes exactly one argument (2 given)

# TypeError: unhashable type: 'list'
# my_set.add(["salmanpour"])
# print(my_set)

# remove
# Remove an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.
# KeyError: 100
my_set.remove(1)
print(my_set)

# discard 
# Remove an element from a set if it is a member.
# If the element is not a member, do nothing.
my_set.discard(100)
print(my_set)


# Remove and return an arbitrary set element.
# Raises KeyError if the set is empty.
item = my_set.pop()

print(item)
print(my_set)

for item in my_set:
    print(item)

# Remove all elements from this set.
my_set.clear()
print(my_set)