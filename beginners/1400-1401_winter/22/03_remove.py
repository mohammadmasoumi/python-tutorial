d = {
    "k1": "v1",
    "k2": "v2",
}

# 1.
value = d.pop("k1")
print(value, d)

# 2. del
del d["k2"]
# del d

print(d)