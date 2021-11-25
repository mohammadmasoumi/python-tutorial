"""
student info

500 students



"""

data = {
    # 'sara': {}
    # wrong because we might have two sara's
    'Sarah-Asghari': '041054347',
    'Sarah-Asghari-moghadam': '021054347',
}

national_id = '041054347'

# key, value = (key, value) # unpacking
# key, value = ('Sarah-Asghari', '041054347') # unpacking
for key, value in data.items():
    if value == national_id:
        print(key)
