d = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "k4": "v4",
}

d["k1"] = "v10"  # update
d["k5"] = "v5"  # add

print(d)

k3 = "v20"
k6 = "v12"
# update(key=value)
d[k6] = "k6"  # d["v12"] = "k6"
d["k6"] = "k6"  # d["v12"] = "k6"

# NameError: name 'k3' is not defined
d[k3] = "k7"  # k3 = "v20"
d["v20"] = "k7"  # k3 = "v20"

d["k3"] = "k7"
d["k10"] = "k7"

print(d)
d["k6"] = "k6"
d.update(k6="k6")
d.update(k3="k6")
print(d)
