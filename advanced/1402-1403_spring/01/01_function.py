# Application

# 1. Reusable
# 2. Break down logic
# 3. Description

# burst
# move
# move_right

"""
prototype 
signature

built-in function:
    - print

keywords(reserved keys) 
    - def
    - class
    - if
    - else
    - elif
    - and or not
    - in

camelCase
[*]snake_case
[*]PascalCase

args = [0:OO]
return = [1: OO]

def [function_name](args): 
    function body
    return []

scopes:
    - global
    - nonlocal
    - local

"""

# [1]
# a, b: args
def add(a, b):
    # [3]
    # a: 12
    # b: 13
    # [4]
    c = a + b
    return c

# 12, 13 params
# [2]
# call invoke
print(add(12, 13)) # [5]
print(add(12, 13)) 

a, b = 12, 13
if add(a, b):
    print("Hello")

# truthy falsy
# if CONDITION
# if a:
# if bool(a):

# return None

# default value for return: None
def f1():
    a = 12

def f2():
    a = 12
    return 
    
def f3():
    a = 12
    return None

def multi_return():
    return 12
    # unreachable
    print("Hello") # doesn't execute this line

def multi_return():
    return 12
    return 13
    return 14

multi_return()