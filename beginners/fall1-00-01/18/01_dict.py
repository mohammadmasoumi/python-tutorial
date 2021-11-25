# dict

"""
Attributes:
    Changeable
    Repetitive keys - last value
    Ordered or unordered? < python 3.7 ordered
"""

# student

student_info = {
    # key-value pair
    'name': 'Asghar',
    'last_name': 'Asghari',
    'age': 16,
    'national_code': 1231232432,
    'avg': 19.2,
    'father_name': 'Akbar',
    'is_male': True,
    'gender': 'Male',  # Female
}

# pop from the end of the dict
# ('gender', 'Male') tuple
# Remove and return a (key, value) pair as a 2-tuple.
item1 = student_info.popitem()
item2 = student_info.popitem()

# value = pop(key)
item3 = student_info.pop('age')

"""
student_info = {
    # key-value pair
    'name': 'Asghar',
    'last_name': 'Asghari',
    'national_code': 1231232432,
    'avg': 19.2,
    'father_name': 'Akbar',
}
"""

print(item1)
print(item2)
print(item3)

print(f"student_info: {student_info}")

# update / add
student_info.update(father_name='Abbas')  # update
student_info.update(grand_father='Akbar Jn')  # update

# pop key-value
father_name = student_info.pop('father_name')

print(f"father_name: {father_name}")
print(f"student_info: {student_info}")
