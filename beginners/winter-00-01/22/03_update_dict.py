my_dict2 = {
    'key1': 'value1',
}

# update/insert value
# list
# my_dict2[0] = 'akbar'
# 1.
my_key = 'key1'
ur_key = 'ur_key'
# my_dict2['key1'] = 'asghar'
# NameError: name 'my_key' is not defined
# update
my_dict2[my_key] = 'asghar'
print(my_dict2)

# insert
my_dict2[ur_key] = 'asghar'
print(my_dict2)

# 2. 
my_dict2.update(my_key='akbar')
print(my_dict2)

my_dict2.update(key1='akbar')
print(my_dict2)

my_dict2.update(key2='akbar')
print(my_dict2)






