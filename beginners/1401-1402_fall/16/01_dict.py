dict1 = {"k1": "v1", "k2": "v2"}
dict2 = {"k1": "v3", "k2": "v4"}

dict1.update({"k5": "v5", "k1": "v6"})
print(dict1)
dict1.update(dict2)
print(dict1)

key1 = "k10"
value1 = "v10"
dict1.update(key1=value1)

# dict1["k10"] = "v10"
dict1[key1] = value1
# dict1.update({"k10": "v10"})
dict1.update({key1: value1})

print(dict1)

key2 = "k11"
value2 = {"k20": "v20"}

dict1[key2] = value2
dict1.update({key2: value2})
print(dict1)
