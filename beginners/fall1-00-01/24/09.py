d = {
    'name': 'ali',
    'info1': {
        'age1': 20,
        'info2': [2, 3, {'a': {'b': 12}}]
    }
}
print(d.get('info1').get('info2')[1].get('a').get('b'))


"""
output:

AttributeError: 'int' object has no attribute 'get'
"""