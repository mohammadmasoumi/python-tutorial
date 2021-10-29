# remove
dict1 = {
    "a": 1,
    "b": 1,
}

# pop - key
# dict1.pop("a")
value = dict1.pop("a")
print(value)
print(dict1)

# del
del dict1["b"]
# del dict1 - delete whole object
# del dict1 - you can use dict1 any more

print(dict1)

# pop items - random pop
# KeyError: 'popitem(): dictionary is empty'
# dict1.popitem()
print(dict1)

dict1["c"] = 2

# clear
print(dict1)
dict1.clear()
print(dict1)
