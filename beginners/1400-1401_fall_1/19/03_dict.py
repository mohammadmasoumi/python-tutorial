d = {}

key = "name"

d.update(name="ali")  # key: key, value: ali
d.update(key="ali")  # key: key, value: ali

d[key] = "ali"  # key: name, value: ali
d["name"] = "ali"  # key: name, value: ali

print(d)
