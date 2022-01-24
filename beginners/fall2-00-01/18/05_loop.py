# loop over dict

data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

# loop over keys
for key in data:
    print(key)

print("----------------------")
# loop over keys
for key in data.keys():
    print(key)

print("----------------------")
# loop over values
for value in data.values():
    print(value)

print("----------------------")
# loop over keys and values
for key, value in data.items():
    print(f"key: {key}, value: {value}")