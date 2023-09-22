"""
Set

1. unordered -> you can't use index | items are immutable
2. mutable -> add, discard, ...
3. duplication is not allowed
4. items must be hashable

hashable:
    - int
    - str
    - bool
    - float
    - tuple | items must be immutable

unhashable:
    - list
    - set
    - tuple | list or set included
"""

empty_tuple = tuple() # ()
empty_set = set() # {}

# dict_ = {}
# print(type(dict_))

my_set1 = {1, 1, 1, 2, 3, 4}
print(my_set1)

