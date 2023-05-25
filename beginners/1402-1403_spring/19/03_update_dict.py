
d = {
    'k1': 'v1',
    'k2': 'v2'
}

# my_list = [1, 2, 3]
# my_list[0] = 100

# update and insert => upsert
# d[key] = new value

# if key exists => update value
# else => insert new pair of key value
d['k1'] = 'new v1'
d['k100'] = 'new v100'

print(d)

d = {}
# update function
key = "k10"
value = "v10"

# "key": "v10"
d.update(key=value) # => d.update(key="v10")
d.update(value=key)

# "k10": "v10"
d[key] = value # => d["k10"] = "v10"
# d[key1] = value1 # Exception
d.update(asghar="value")

print(d)