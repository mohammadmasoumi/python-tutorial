dict1 = {"a": 1, "b":2}
dict2 = {"c": 3, "d":4}

# TypeError: unsupported operand type(s) for &: 'dict' and 'dict'
# print(dict1 & dict2)

# merge
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1 | dict2)

# TypeError: unsupported operand type(s) for ^: 'dict' and 'dict'
print(dict1 ^ dict2)
