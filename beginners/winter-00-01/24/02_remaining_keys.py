d = {
    "name": "ali",
    "salary": 2000,
    "city": "varamin",
    "nationality": "IR"
}
remaining_keys = ["name", "salary"]
d_copy = {**d}

# for key in d.keys():
#     # membership operator
#     # in, not in 
#     if key not in remaining_keys:
#         d.pop(key)

for key in d_copy.keys():
    # membership operator
    # in, not in 
    if key not in remaining_keys:
       d .pop(key)

for key in list(d.keys()):
    # membership operator
    # in, not in 
    if key not in remaining_keys:
        d.pop(key)

new_d = {}
for key in remaining_keys:
    new_d[key] = d.get(key)


print(d.keys())
print(d)