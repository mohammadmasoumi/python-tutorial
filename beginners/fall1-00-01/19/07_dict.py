d = {
    'name': 'ali',
    'info1': {
        'age1': 20,
        'info2': {
            'age2': 21
        }
    }
}

print(d.get('name'))

info1 = d.get('info1')
info2 = info1.get('info2')
print(info2.get('age2'))

print(d.get('info1').get('info2').get('age2'))

# print(d['info2'])
