# remove

d = {
    'k1': 'v1',
    'k2': 'v2',
}

# pop
# (__key: str, /) -> str
# D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
# If the key is not found, return the default if given; otherwise, raise a KeyError.
value = d.pop('k1')  # pop key, value pair
print(f"popped value: {value}")
print(d)

# KeyError: 'k10'
# value = d.pop('k10')  # pop key, value pair
# print(f"popped value: {value}")
# print(d)

default_value = 'v10'
value = d.pop('k10', 'default value')
value = d.pop('k10', default_value)  # pop key, value pair
print(f"key: 'k10', popped value: {value}")
print(d)

# TypeError: pop expected at least 1 argument, got 0
# value = d.pop()

# ('k2', 'v2')
# popped (key, value)
popped_value = d.popitem()
print(f"popped_value: {popped_value}")

#
# d.keys()
# d.values()
# d.items()

# del
print("------- DEL -------")
d = {
    'k1': 'v1',
    'k2': 'v2',
}

del d['k1']  # d.pop('k1')
print(d)

# KeyError: 'k10'
# del d['k10']
# print(d)

# del d
# # NameError: name 'd' is not defined. Did you mean: 'id'?
# print(d)

# AttributeError: 'dict' object has no attribute 'remove'
# d.remove()
# print(d)
