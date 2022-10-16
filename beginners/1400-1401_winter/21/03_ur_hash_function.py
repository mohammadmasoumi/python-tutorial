from random import randint
#                   start: end
# Return random integer in range [a, b], including both end points.
random_num = randint(10000000, 10000000000000)

def my_hash(value):
    
    if isinstance(value, bool):
        return 1 if value else 0

    elif isinstance(value, int):
        return value

    elif isinstance(value, float):
        return value * random_num * pow(10, 6)

    elif isinstance(value, str):
        # ali 
        # ila
        # lai
        hashed_value = 1
        for idx, character in enumerate(value):
            hashed_value += ord(character) * (idx + 1) * random_num
        
        return hashed_value

    elif isinstance(value, tuple):
        hashed_value = 1
        for idx, item in enumerate(value):
            hashed_value += my_hash(item) * (idx + 1) * random_num

        return hashed_value
    else:
        raise ValueError(f"unhashable type {type(value)}")


print(my_hash(True))
print(my_hash(False))
print(my_hash(12))
# print(my_hash(12.2))
print(my_hash("ali"))
print(my_hash("ali"))
print(my_hash("ial"))
print(my_hash((1, 2)))
print(my_hash((1, 2)))
print(my_hash((1, 2)))
print(my_hash((2, 1)))
# print(my_hash([1, 2]))
# print(my_hash((2, [1, 2])))