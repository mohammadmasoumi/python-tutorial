# methods on dict
d = {
    'a': 1,
    'b': 2
}

# if key exist: nothing happen
# otherwise: insert key and default value
d.setdefault('b', 3)
d.setdefault('c', 3)

# d.get('b'): 2
# if not 2: false
if not d.get('b'):
    d['b'] = 3

# d.get('c'): None
# not d.get('c'): Not None: True
if not d.get('c'):
    d['c'] = 3

# value: falsy value
d = {
    'a': 1,
    'b': 0
}

# d.get('b'): 0
# not 0: true
if not d.get('b'):
    d['b'] = 3

#
if d.get('b') == None:
    d['b'] = 3

# if key doesn't exist
if 'b' not in d:
    d['b'] = 3


print(d)

# fromkeys
# d = {
#     'a': 1,
#     'b': 2
# }
keys = {'b', 'c', 'd'}
new_dict = dict.fromkeys(keys, 'new value')
print(new_dict)
