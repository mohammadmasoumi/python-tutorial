import string
from random import randint


def default_value_with_list(value=[]):
    value.append(10)
    print(f"value: {value}, id(value): {id(value)}")


default_value_with_list()
default_value_with_list()
default_value_with_list()


def default_value_with_dict(value={}):
    random_num = randint(0, 25)
    key = string.ascii_lowercase[random_num]
    print(f"key: {key}")
    value[key] = 1
    print(f"value: {value}, id(value): {id(value)}")


default_value_with_dict()
default_value_with_dict()
default_value_with_dict()


def default_value_with_set(value=set()):
    random_num = randint(0, 20000)
    value.add(random_num)
    print(f"value: {value}, id(value): {id(value)}")


default_value_with_set()
default_value_with_set()
default_value_with_set()