# assignment 3

sample_dict = {
    "name": "Kelly",
    "age": 20,
    "salary": 20000,
    "city": "NY",
}

keys_to_remain = ["name", "salary"]
keys_to_remove = ["age", "city"]

# pop - remove key and return it's value
# list => .pop(index)
# value = dict.pop(key)

# solution 1
# for key in keys_to_remove:
#     value = sample_dict.pop(key)
#     print(value)

# solution 2
new_sample_dict = {}
for key in keys_to_remain:
    # print(f"key: {key}, value: {sample_dict[key]}")
    new_sample_dict[key] = sample_dict[key]
    # new_sample_dict[key] = sample_dict.get(key)
    # print(new_sample_dict)

print(new_sample_dict)
print(sample_dict)





