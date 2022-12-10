dict1 = {"k12": "v1", "k22": "v2"}

# keys
print("-----------------------------")
for item in dict1:
    print(item)

print("-----------------------------")
# k1 , k2
# item1, item2 = k1
#                 ["k", "1", "2"]
# item1, *item2 = "k12"
for item1, *item2 in dict1:
    print(item2)

# keys
print("-----------------------------")
for key in dict1.keys():
    print(key)

# values
print("-----------------------------")
for value in dict1.values():
    print(value)

# keys, values
print("-----------------------------")
for key, value in dict1.items():
    print(key, value)


keys = list(dict1.keys())
values = list(dict1.values())
items = list(dict1.items())

print(keys)
print(values)
print(items)