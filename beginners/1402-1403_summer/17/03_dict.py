my_dict1 = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = {'a': 10, 'd': 20}
# my_dict1.update(key=20)
# my_dict1.update(my_dict2)  # dict1: {'a': 10, 'b': 2, 'c': 3, 'd': 20}
# print(my_dict1)
print(my_dict2.update(my_dict1))
print(my_dict2) # dict2: {'a': 1, 'b': 2, 'c': 3, 'd': 20}
"""
my_dict2.update(my_dict1)
{
    'a': 10,  # 1
    'd': 20,

    # 'a': 1, 
    'b': 2, 
    'c': 3
}
"""