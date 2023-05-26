# copy
from copy import deepcopy

d5 = {'k1': 'v1'}
d6 = dict(d5)  # create new dict d5
d7 = {**d5}
d8 = d5.copy()

print(id(d5), id(d6), id(d7), id(d8))


# shallow copy vs deep copy
print(f"------ SHALLOW COPY ------")

# Shallow copy
d1 = {
    'k1': [1, 2, 3],
    'k2': 'v2'
}

d2 = d1.copy()

print(f"id(d1):{id(d1)}, id(d2): {id(d2)}")
print(f"id(d1['k1']):{id(d1['k1'])}, id(d2['k1']): {id(d2['k1'])}")

# d2['k1']: [1, 2, 3]
# d2['k1']: list
d2['k1'].append(4)

print(d1, d2)

# Deep copy
print(f"------ DEEP COPY ------")

d1 = {
    'k1': [1, 2, 3],
    'k2': 'v2'
}

d2 = deepcopy(d1)
print(f"id(d1):{id(d1)}, id(d2): {id(d2)}")
print(f"id(d1['k1']):{id(d1['k1'])}, id(d2['k1']): {id(d2['k1'])}")

# d2['k1']: [1, 2, 3]
# d2['k1']: list
d2['k1'].append(4)

print(d1, d2)
