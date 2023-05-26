# loop over

d = {
    'k_1': 'v1',
    'k_2': 'v2',
    'k_3': 'v3',
    'k_4': 'v4',
    'k_5': 'v5',
}

# loop over keys
for key in d:
    print(key)

# unpacking
a, *b = 'ali'  # ['a', 'l', 'i']
# a: 'a'
# b: ['l', 'i']

for a, *b in d:
    # a, *b = 'k1'
    # a: k, b: ['_', '1']
    print(f"a: {a}, b: {b}")

# keys
for key in d.keys():
    print(key, d.get(key))

# D.keys() -> a set-like object providing a view on D's keys
keys = d.keys()
# dict_keys(['k_1', 'k_2', 'k_3', 'k_4', 'k_5'])
print(keys)

keys = list(d.keys())
print(keys)

# values
for value in d.values():
    print(value)

values = d.values()
# dict_values(['v1', 'v2', 'v3', 'v4', 'v5'])
print(values)

values = list(d.values())
print(values)

# key value
# [(key, value), (key, value), (key, value)]
for key, value in d.items():
    # key, value = (key, value)
    print(f"key: {key}, value: {value}")

print(d.items())
print(list(d.items()))
