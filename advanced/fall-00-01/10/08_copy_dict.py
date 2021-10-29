d = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# 2589764163584
# 2589764163584
# put d1 label on box
d1 = d

print(id(d))
print(id(d1))

d1.update(d=4)
print(d)
print(d1)

d2 = d.copy()
d3 = {**d}
