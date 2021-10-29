d = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key, value in d.items():
    print(f"key: {key}, value: {value}")

print("------------------------")
for key in d.keys():
    print(f"key: {key}")

print("------------------------")
for value in d.values():
    print(f"value: {value}")

print("------------------------")
# just keys
for item in d:
    print(item)
