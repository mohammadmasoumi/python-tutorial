# for loop

d = {
    "key1": "value1",
    "key2": "value2"
}

# just keys
# ["key1", "key2"]
for key in d:
    print(key)

print("-----------------------")
# just keys
# ["key1", "key2"]
for key in d.keys():
    print(key)

print("-----------------------")
# just value
# ["value1", "value2"]
for value in d.values():
    print(value)

print("-----------------------")
# key, value
for key, value in d.items():
    print(f"{key}: {value}")

print("-----------------------")
# key, value
for item in d.items():
    # ('key1', 'value1')
    # ('key2', 'value2')
    key, value = item
    print(key, value, item)