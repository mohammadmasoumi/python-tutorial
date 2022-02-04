# data types
# int , bool, str, float, tuple, list, dict, set
# built-in function, max, min, sum, int, list, dict
# django is a framework
# virtual env
# pip install virtualenv
# python(3) -m virtualenv [name of virtual]
# Directory of C:\Users\MFT\Desktop\advanced_pytthon
# .\[virtualenv name]\Scripts\activate
# (my_venv) C:\Users\MFT\Desktop\advanced_pytthon>
# project direction
# python -m virtualenv my_env
# pip install django

# list
# list comprehension
# item % 2
# item = 2 => item % 2 = 0 => if 0 => False
# item = 3 => item % 2 = 1 => if 1 => True 

list_comprehension1 = [item * 2 for item in [1, 2, 3, 4] if item % 2]
print(list_comprehension1)

# // => floor divition, no precision
# / => with precition
list_comprehension2 = [item * 2 if item % 2 else item // 2 for item in [1, 2, 3, 4]]
print(list_comprehension2)

my_2d_list = [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3, 4, 5, 6]
#                             items = [1, 2, 3], [4, 5, 6]
#                             item = 1, 2, 3       4, 5 ,6
list_comprehension3 = [item for items in my_2d_list for item in items]
print(list_comprehension3)

# range index - slicing
#          -6 -5 -4 -3 -2 -1
#          0  1  2  3  4  5
my_list = [1, 2, 3, 4, 5, 6]

# [start: end(no included): step]
print(my_list[2: 4: 2])
print(my_list[-5: 0: 1]) # empty
print(my_list[-5: 0: -1]) # [2]

# append
my_list.append(7)
my_list.append([1, 2, 3]) # add as one item
# TypeError: list.append() takes exactly one argument (3 given)
# my_list.append(1, 2, 3)
my_list.extend([8, 9, 10])
my_list.extend([8, 9, [1, 2, 3]])
# [1, 2, 3, 1] 
# [2, 3, 1] remove first occurance of item
my_list.remove(1) # item - remove first occurance of item
item1 = my_list.pop() # remove last item
item2 = my_list.pop(0) # remove indexes item
print(my_list)

# dict
dict_comprehension1 = { key: value for key, value in {"key1": "value1", "key2": "value2"}.items() if key == "key1" }
print(dict_comprehension1)
# no if else

dict1 = {
    # key      value
    "name": "Asghar",
    "last_name": "Asghari",
    "name": "Akbar" # update the value of `name` key
}

print(dict1)

# access to element

# 1. variable_name.get(key, default_value)
# if "name" in dict1.keys():
#   return dict1["name"]
# else:
#   return "default_value"
print(dict1.get("name", "default_value"))

# 2. variable_name[key] | brackets 
print(dict1["name"])
# Traceback (most recent call last):
#  File "C:\Users\MFT\Desktop\advanced_pytthon\01\01_review.py", line 85, in <module>
#    print(dict1["key_does_not_exist"])
# KeyError: 'key_does_not_exist'
print(dict1["key_does_not_exist"])

# update key value in dict
key = "last_name"
dict1["last_name"] = "new last name1"
dict1[key] = "new last name"

dict1.update(last_name="new last name2")
dict1.update(key="new last name2")
print(dict1)

# remove key
# pop
item3 = dict1.pop("key")
#                    key       default_value (int, str, list, tuple, ...)
item4 = dict1.pop("asghar", "default_value")
# if key does not exist, return default value
# if "akbar" in dict1:
#   item5 = value of "akbar" | dict1["akbar"]
# else:
#   item5 = "default_value" | [1, 2, 3]
item5 = dict1.pop("akbar", [1, 2, 3])
del dict1["last_name"]
print(item3)
print(item4)
print(item5)
print(dict1)

# * => multiply
# ** => power

print(2 ** 3)
