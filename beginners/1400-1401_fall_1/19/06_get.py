d = {
    'name': 'ali',
    'last_name': 'alavi'
}

print(d.get('name'))
print(d.get('father_name'))

#             key       default value
print(d.get('father_name', 'abbas'))
# d.update(father_name='abbas')

# print(d['father_name'])  # KeyError: 'father_name'
