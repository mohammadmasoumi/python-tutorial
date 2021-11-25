d = {'a': 12, 'b': 13, 'c': 14, 'd': 15, 'e': 16}

# readability
d1 = {
    'a': 12,
    'b': 13,
    'c': 14,
    'd': 15,
    'e': 16
}

# 1
# for key, value in d.items():
#     print(f"{key}: {value}")
#     print(f"key: {key}, value: {value}")

# 2
# ('a', 12) tuple
for item in d.items():
    # ('a', 12)
    # key: 'a'
    # value: 12
    key, value = item
    print(item, key, value)
