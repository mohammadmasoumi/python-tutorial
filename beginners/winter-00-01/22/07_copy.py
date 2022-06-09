# copy
from copy import deepcopy

d1 = {
    'key1': 'value1',
    'key2': 'value2',
    'key4': [1, 2]
}

# {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# d2 = d1
# d1.update(key3='value3')

# print(d1)
# print(d2)
print("--------------------------------------")

# d2 = d1.copy()
# d1.update(key3='value4')

# print(d1)
# print(d2)
print("--------------------------------------")

# d2 = d1.copy()
# d1['key4'].append(3)

# print(d1)
# print(d2)

d2 = deepcopy(d1)
d1['key4'].append(3)

print(d1)
print(d2)


