from functools import total_ordering
from random import randint

from attr import has

def multiply(string):
    total = 1
    for char in string:
        total *= ord(char)
    
    return total


hash_dict = {}

def my_hash(value):

    if isinstance(value, int):
        hash_value = hash_dict.get(value, value * randint(0, 1000) + 100)
        hash_dict[value] = hash_value

    elif isinstance(value, float):
        hash_value = hash_dict.get(value, value * randint(0, 10000) // 3 + 200)
        hash_dict[value] = hash_value
    
    elif isinstance(value, str):
        hash_value = hash_dict.get(value, multiply(value))
        hash_dict[value] = hash_value
    else:
        print(f"{type(value)} is not hashable!")

    return hash_value


print("10: ", my_hash(10))
print("10: ", my_hash(10))
print("10.2: ", my_hash(10.2))
print("True: ", my_hash(True))
print("ali: ", my_hash("ali"))
print("ali: ", my_hash("ali"))
