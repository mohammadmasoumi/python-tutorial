# pop/delete

# pop
# D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
# If the key is not found, return the default if given; otherwise, raise a KeyError.
d = {
    'a': 1,
    'b': 2,
    'c': 3
}

# 1.
key = 'a'
value = d.pop(key)

print(f"value: {value}")
print(f"d: {d}")

# 2.
# KeyError: 'funzy'
# key = 'funzy'
# value = d.pop(key)

# print(f"value: {value}")
# print(f"d: {d}")

# 3.
key = 'a'
value = d.pop(key, 'default value')

print(f"value: {value}")
print(f"d: {d}")

# popitem
# pop the last value
value = d.popitem()
print(f"value: {value}")
print(f"d: {d}")
print("------------------")

# delete
d = {
    'a': 1,
    'b': 2,
    'c': 3
}

del d['a']
print(d)

# KeyError: 'funzy'
# del d['funzy']
# print(d)

# NameError: name 'd' is not defined. Did you mean: 'id'?
# remove d variable
# del d
# print(d)
print("------------------")

# clear
d = {
    'a': 1,
    'b': 2,
    'c': 3
}

d.clear()
print(d)
