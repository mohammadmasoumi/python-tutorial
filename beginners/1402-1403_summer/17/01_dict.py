# dict

"""
1. mutable
2. ordered (3.6)
3. duplication key is not allowed

# 
k1 -> v1
k1 -> v2

{
    word: definition
    key: value
}

{
    'name': 'asghar'
    'age': 22,
    'scores': [20, 10]
}

keys must be hashable.
"""
# empty dict
d = {}

# instead of
#      0     1      2
# ['asghar', 22, [20, 10]]
student = {'name': 'asghar', 'age': 22, 'scores': [20, 10]}
student = {
    'name': 'asghar',
    'age': 22,
    'scores': [20, 10],  # the last comma is optional
}
"""
JSON - javascript object notation
{
    "name": "asghar",
    "age": 22,
    "scores": [20, 10]
}
"""
"""
[      key     value
    ('name', 'asghar'), 
    ('age', 22), 
    ('scores', [20, 10])
]

"""
student = dict([('name', 'asghar'), ('age', 22), ('scores', [20, 10])])


# access to the value
# 1. [] barackets
print(student['name'])
print(student['age'])
print(student['scores'])

# key = input()
key = 'name'
print(student[key])

# KeyError: 'doesnotexist'
# print(student['doesnotexist'])
# print(student['k'])
# print(student['lastname'])

# 2. .get
# key -> value
# name -> asghar
print(student.get('name'))
print(student.get('fox'))

# default value
#                   key, default value
print(student.get('fox'))  # default value: None
print(student.get('fox', 'default value'))
# if key exists -> return the value of key
# otherwise -> return default value
print(student.get('fox', 'mohammad'))

# keys must be hashable.
# TypeError: unhashable type: 'list'
# d = {
#     [1, 2]: 'a',
#     {1, 2}: 'b',
#     ([1, 2], 3): 'c',
#     {'a': 'b'}: 'd'
# }

# print(d.get([1, 2]))
