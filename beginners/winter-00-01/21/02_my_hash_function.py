from random import randint
from time import time


random_number = randint(1, 10000)
current_time = time()

def my_hash(value):

    if isinstance(value, bool):
        return 1 if value else 0

    elif isinstance(value, int):
        return value

    elif isinstance(value, str):
        hashed_value = 0
        for idx, character in enumerate(value):
            hashed_value += (ord(character) * (idx + 1)) * random_number * current_time

        return hashed_value
    
    elif isinstance(value, float):
        return value * value * current_time
    
    elif isinstance(value, tuple):
        hashed_value = 1
        for idx, item in value:
            hashed_value += (idx + 1) * my_hash(item)
        
        return hashed_value 
    else:
        raise ValueError(f"unhashable type {type(value)}")


print(my_hash(12))
print(my_hash(12.1))
print(my_hash("ali"))
print(my_hash("ali"))
print(my_hash("ila"))
print(my_hash("ila"))
print(my_hash("ial"))
print(my_hash(True))
print(my_hash(False))