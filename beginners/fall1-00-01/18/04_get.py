d = {
    'a': 10,
    'b': 11
}

# get(key, default_value)

"""
1. key exists:
value = d.get('a', 20)
# value: 10 

2. key does exist
value = d.get('c', 20)
# value: 20
"""

value1 = d.get('a', 20)
#              key, default value
value2 = d.get('c', 20)

print(f"value1: {value1}")
print(f"value2: {value2}")
print(d)
