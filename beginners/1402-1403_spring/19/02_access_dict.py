
d1 = {
    'k1':'v1',
    'k2':'v2',
}

# Access 

# brackets
print(d1['k1'], d1['k2'])
# print(d1['asghar']) # KeyError: 'asghar'

print(d1.get('k1'))
print(d1.get('k2'))

# nil null none 
print(d1.get('asghar')) # None , HICHI
print(d1.get('asghar'))

# (__key: str, __default: str | _T@get, /
#                      default value

# if key exists -> the value of key
# if key does not exist -> default value 
print(d1.get('asghar', 'water'))
print(d1.get('asghar', 'v3'))
print(d1.get('asghar'))


d1 = {
    'key': 'value',
    'akbar': 'value'
}

# dynamic key
key = 'asghar'
default_value = 'value'
#               key  default value
value = d1.get(key, default_value) # => d1.get('asghar', 'value') 
 
# akbar: value
print(f"{key}: {value}")
