from ecdsa import keys


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}


deleting_keys = ["age", "city"]
remaining_keys = ["name", "salary"]

# solution 1 - remove extra keys from existing dict
# .pop
# value = dict.pop(key)
# for key in deleting_keys:
#     value = sample_dict.pop(key)
#     print(value)

# print(sample_dict)

# solution 2 - create a new dict with remaining keys
# .get
# value = dict.get(key)
new_dict = {}
for key in remaining_keys:
    new_dict[key] = sample_dict[key]

print(new_dict)