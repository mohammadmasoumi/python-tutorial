# function 
"""
keyword: def, return

functions are variable

1. alphanumeric and underscore/underline[_](it only contains alphabetic and numerics)
2. mustn't start with digits
3. not -> @ # $ % ...
4. snakecase convenstion 

# declare, definition, prototype
                    a, b, c
                    a, b
                    a
def [FUNCTION_NAME](PARAMS[comma separated]):
    # Function body
    # do sth
    return a + b


FUNCTION(ARGS)
----
return None 

def func():
    pass

def func():
    return

def func():
    return None
"""

#      params
def add(a, b): # a: 10, b: 12
    return a + b

def add_without_return(a, b):
    a + b

res = add(10, 12) # arguments
res_without_return = add_without_return(10, 12)

print(f"res: {res}")
print(f"res_without_return: {res_without_return}")