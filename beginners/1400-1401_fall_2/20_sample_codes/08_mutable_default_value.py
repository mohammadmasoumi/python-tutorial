# be careful with list, dict and set as default value
from random import randint
from string import ascii_lowercase


def function_with_list_as_default_value(a=[]):
    a.append(10)
    print(f"a: {a}, id(a): {id(a)}")
    return a


# be careful
function_with_list_as_default_value()
function_with_list_as_default_value()
function_with_list_as_default_value()
function_with_list_as_default_value()
print("--------------------------------")


def function_with_dict_as_default_value(a={}):
    key = ascii_lowercase[randint(0, 25)]
    a[key] = 1
    print(f"a: {a}, id(a): {id(a)}")
    return a


function_with_dict_as_default_value()
function_with_dict_as_default_value()
function_with_dict_as_default_value()
function_with_dict_as_default_value()
print("--------------------------------")


def function_with_set_as_default_value(a=set()):
    a.add(randint(0, 25))
    print(f"a: {a}, id(a): {id(a)}")
    return a


function_with_set_as_default_value()
function_with_set_as_default_value()
function_with_set_as_default_value()
function_with_set_as_default_value()
print("--------------------------------")
