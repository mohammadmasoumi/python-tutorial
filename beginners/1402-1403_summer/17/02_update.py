# update

# update + insert -> upsert
d = {'a': 1}

# if key exists -> update it's value
# otherwise -> add key:value
d['b'] = 2  # insert
print(d)
d['b'] = 3  # update
print(d)

#
d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'b': 4  # update `b` value
}
"""
d = {
    'a': 1,
    'b': 2,
    'c': 3
}
d['b'] = 4
"""
print(d)

# update
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
key = 'd'
value = 4
# key, value are variables
my_dict[key] = value
# my_dict['d'] = 4
print(my_dict)

# update - update is a function
# keyword argument
# "key": value
# key is not variable
my_dict.update(key=value)
my_dict.update(asghar=value)
my_dict.update(a=value)
print(my_dict)

# update - key is variable
my_dict.update({key: value})
my_dict.update({'a': 1, 'b': 2})
