d = {
    'name': 'ali',
    'age': 20,
    'grade': 10,
    'city': 'vancover'
}

# ['name', 'city']

remaining_keys = ['name', 'city']

print({k: v for k, v in d.items() if k in remaining_keys})
