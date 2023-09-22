# loop over dictionary

d = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
    'k4': 'v4'
}

# 1. loop over dict
for item in d:
    # item ?
    # item: 'k1': 'v1'
    # item: 'v1', 'v2'
    # item: ('k1', 'v1')
    # item: 'k1', 'k2'
    # item: ['k1', 'v1']
    print(item)

print("-------------")
# 
for key, value in d:
    # key, value = 'k1' 
    # key: 'k', value: '1'
    
    # key, value = 'k2' 
    # key: 'k', value: '2'

    # item ?
    # item: 'k1': 'v1'
    # item: 'v1', 'v2'
    # item: ('k1', 'v1')
    # item: 'k1', 'k2'
    # item: ['k1', 'v1']
    print(key, value)

print("-------------")
# 2. .keys
for key in d.keys():
    print(key, d[key])


print("-------------")
# 3. .values
for value in d.values():
    print(value)


print("-------------")
# 3. .items
for key, value in d.items():
    print(key, value)


print("-------------")

