"""
-- INTRODUCTIONS --

function 

keyword: def
datatype: func
functions are variables

params:
    - # of inputs: 0 or oo
    - # of outputs: 1 or oo

def FUNCTION_NAME(PARAMS):
    # function body
    # function block
    return 

-- CONCEPTS --

1. function vs method
    ----
    - methods on objects
    - function stand alone
    ----

2. params vs arguments
    ----
    def add(a, b): # a, b params
        return a + b

    add(10, 12) # 10, 12 args
    ----

[{
    'name': 'asghar',
    'age': 20
}]

# OOP object oriented programming
class Student:

    # method 
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student('asghar', 20)
student.name
student.age

-- APPLICATIONS --
    - reusable code 
    - enhance code readability
    - decrease bug or making mistakes
    - break down logic
"""

# برنامه نمیدونه کدوم خط رو اجرا کنه
a1, b1 = 12, 13
c1 = a1 + b1

a2, b2 = 12, 13
c2 = a2 + b2 + 1

# naming conventions
#   - snake_case [x]
#   - camelCase
#   - PascalCase  

# define variable named  add
# function prototype
# add(a, b) -> function signature

# typing
# : int 
# -> int
def add(a: int, b: int) -> int:
    # a: "ali"
    # b: "asghar"
    # a + b => concate
    # "aliasghar"

    # a: "ali"
    # b: "reza"
    return a + b


# call
# invoke
# (a: Any, b: Any) -> Any
print(add("ali", "asghar"))
print(add("ali", "reza"))