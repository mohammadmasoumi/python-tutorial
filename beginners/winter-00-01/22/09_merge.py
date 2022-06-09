# merge

d1 = {
    'k1': 'v11',
    'k2': 'v2'
}

d2 = {
    'k1': 'v12', 
    'k3': 'v3'
}


"""
d1.update(d2)
{
    # 'k1': 'v11',
    'k2': 'v2',
    'k1': 'v12', 
    'k3': 'v3'
}

d2.update(d1)
{
    # 'k1': 'v12', 
    'k3': 'v3',
    'k1': 'v11',
    'k2': 'v2'
}
"""
# d1.update(d2)
# d2.update(d1)

# print(d1)
# print(d2)

"""
{**d1, **d2}
{
    # 'k1': 'v11',
    'k2': 'v2',
    'k1': 'v12', 
    'k3': 'v3'
}

{**d2, **d1}
{
    'k1': 'v12', 
    'k3': 'v3',
    'k1': 'v11',
    'k2': 'v2'
}
"""
print({**d1, **d2})
print({**d2, **d1})
print(d1)
print(d2)

