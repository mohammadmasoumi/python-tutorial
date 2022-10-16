"""
list:
    - Changeable/Mutable
    - Ordered - index 
    - Allow dubplication [1, 1]
tuple:
    - Unchangeable/Immutable
    - Ordered - index
    - Allow dubplication (1, 1)
"""

a_list = [1, 2] # list
a_tuple = (1, 2) # tuple

a_list.append(3)
# AttributeError: 'tuple' object has no attribute 'append'
# a_tuple.append(3)

# access elem
print(a_list[0])
print(a_tuple[0])

# remove variable
del a_tuple

# NameError: name 'a_tuple' is not defined. Did you mean: 'tuple'?
print(a_tuple)

