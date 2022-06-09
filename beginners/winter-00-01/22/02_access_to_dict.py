my_dict2 = {
    'key1': 'value1',
    'name': 'asghar',
    'age': 12,
    12: 12,
    12.2: 2,
    True: 'asghar',
    (1, 2): 'akbar',
    1: 'mobin',
    12: 13
}

# access to the value
# variable_name[key_name]
print(my_dict2['key1'])
print(my_dict2[12])
print(my_dict2[(1, 2)])

# KeyError: 'city'
# print(my_dict2['city'])

print(my_dict2.get('key1'))
print(my_dict2.get('city'))

# default value
print(my_dict2.get('city', 'default_value'))
print(my_dict2.get('city', 'varamin city'))




