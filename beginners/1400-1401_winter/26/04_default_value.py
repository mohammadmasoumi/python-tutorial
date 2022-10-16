# default value
from random import randint


"""
variable: my_list

params:
    param1: my_list
    default_value1: []
    address1: 0x0012

"""
def append(my_list=[]):
    random_number = randint(0, 100)
    my_list.append(random_number)
    return my_list


# [7]
# [7, 60]
# [7, 60, 58]
# [7, 60, 58, 15]
print(append()) # [100] 
print(append()) # [1]
print(append()) # [2]
print(append()) # [77]
# [100, 1, 2, 77]

def update(my_dict={}):
    random_key = randint(0, 100)
    random_value = randint(0, 100)
    my_dict[random_key] = random_value

    return my_dict

print(update())  
print(update()) 
print(update()) 
print(update()) 