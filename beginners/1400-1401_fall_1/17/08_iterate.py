d = {
    "k1t": "v1",
    "k2t": "v2",
    "k3t": "v3",
    "k4t": "v4",
}

# values
for value in d.values():
    print(value)

print("------------------------------------")
# keys
for key in d.keys():
    print(key)

print("------------------------------------")
# just keys
for item in d:
    print(item)

print("------------------------------------")
# key and value together
for k, v in d.items():
    print(f"{k}: {v}")

print("------------------------------------")

# k, v, t = key
# k, 1, t = k1t
for k, v, t in d:
    print(f"{k} {v} {t}")

print("------------------------------------")
a, b = "xy"
print(a, b)
