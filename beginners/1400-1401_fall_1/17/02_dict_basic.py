# dict

"""
key value

key -> value
key1 -> value
key2 -> value1
"""

"""
immutable -> hashable

0 1 2 3 4 5   6
[          ,value]
"""

# curly braces
# key -> value
# key   # value

"""
1. key must be hashable
2. keys should be unique (last one accepted) 
"""

"""
d = {
    'name': 'hassan',
    1: 10,  # hash(1) = 1
}
d['name']

id1 = hash('name')
id2 = hash(1)

id1 = 0
id2 = 1000

0 1 2 3 4 5 6 7 8 9    ....            1000  
my_list = ['hassan',                                10   ]


d['name']
hash('name') # 0
my_list[0]
"""
d = {
    'name': 'ali',
    'name': 'hassan',
    1: 10,  # hash(1) = 1
    True: 11,  # hash(True) = 1
}

print(d['name'])
print(d[1])

# key as a variable
key = "name"
item = "lastname"

key_value = "ali"
item_value = "karimi"

d1 = {
    # "name": "ali",
    # "lastname": "karimi"
    key: key_value,
    key: "asghar",
    item: key_value,
    item: item_value,
    key: "hassan",
}
print(d1)  # {'name': 'ali', 'lastname': 'karimi'}
print(d1["name"])
print(d1[key])
