"""
student info

500 students



"""

data = {
    # 'sara': {}
    # wrong because we might have two sara's
    'Sarah-Asghari': {
        'father_name': 'majid',
        'national_id': '041054347'
    },
    'Sarah-Asghari-moghadam': {
        'father_name': 'mamad',
        'national_id': '041054747'
    },
}

national_id = '041054347'

# key, value = (key, value) # unpacking
# key, value = ('Sarah-Asghari', {'father_name': 'majid','national_id': '041054347'}) # unpacking
"""
Sarah-Asghari: {'father_name': 'majid', 'national_id': '041054347'}
Sarah-Asghari-moghadam: {'father_name': 'mamad', 'national_id': '041054747'}
"""
for key, value in data.items():
    # key: 'Sarah-Asghari'
    # value: {'father_name': 'majid','national_id': '041054347'}
    # print(f"{key}: {value}")
    # .get(key, default_value)

    # nid1 = value.get('national_id', '08946374')  # exception
    # nid2 = value['national_id']  # exception square brackets

    # comparison operator: bool
    # ==, !=. <=, >=, <, <  ===> bool
    print(value.get('natiaonl_id') == national_id)
    if value.get('national_id') == national_id:
        print(key, value, value.get('national_id'))
