# set

"""
datatypes
    - int
    - str
    - float
    - bool
    - list
        - Ordered [index]
        - Duplicatoin is Allowed [1, 1, 2]
        - Mutable
    - tuple
        - Ordered [index]
        - Duplicatoin is Allowed (1, 1, 2)
        - Immutable
    - set
        - Unordered [You can not use index]
        - Duplicatoin is not Allowed {1, 2}
        - Mutable

built-in function:
    - all()
    - any()
    - int()
    - str()
    - float()
    - print()
    - input()
    - map()
    - filter()
    - list()
    - tuple()
    - max()
    - min()
    - sum()
    - ...
"""
# curly braces
# dict {}
my_set = set()

my_set.add(1)
my_set.add(1)
my_set.add(1)
my_set.add(1)

print(my_set)

my_set1 = {1, 2, 3}
my_set2 = {1}
my_set3 = {}  # dict

print(my_set1)
print(my_set2)
print(type(my_set3))
