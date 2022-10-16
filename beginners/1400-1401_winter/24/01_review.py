d = {
    "key1": "value1",
    "key2": "value2",
    "key1": "value3",
}
print(d)

key = "key1"

# access 
print(d.get("key1"))
print(d["key1"])

print(d.get(key))
print(d[key])

# update -upsert
d.update(key="value4")
d[key] = "value5"

# delete
value = d.pop("key1")
del d["key"]
