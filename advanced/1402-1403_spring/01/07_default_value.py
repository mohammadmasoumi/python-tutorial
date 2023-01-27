def add(a, b):
    return a + b

def add3(a, b, c):
    return a + b + c

print(add(12, 13)) # argument callling
print(add(a=12, b=13)) # keywords callling
# print(add(a=12, c=13)) # keywords callling
print(add(b=13, a=12)) # keywords callling
# TypeError: add() got multiple values for argument 'a'
# print(add(13, a=12))
# print(add(a=12, 13)) # first args then keyword
# print(add(12, a=13))
print(add(12, b=13))
print(add3(12, c=12, b=13))
# TypeError: add3() got multiple values for argument 'b'
# print(add3(12, 12, b=13))


# default value
def add3(a, b=12, c=13):
    return a + b + c

print(add3(11))
print(add3(11, 22))
print(add3(11, c=22))

# -------------------------------------
"""
function1
    [           ]
    [           ]
    [           ]
    [           ]

"""
def function1(a=[]):
    a.append(12)
    return a

my_list = ["Hello"]
print(function1())
print(function1(my_list))
print(function1())
print(function1())

def function2(key, value, a={}):
    # a = {key: value, **a} # create new dict
    a.update({key: value})
    return a

print(function2("k1", "v1"))
print(function2("k2", "v2"))
print(function2("k3", "v3"))
print(function2("k4", "v4"))

def function3(a=(1, 2)):
    return a

print(function3())
print(function3((3, 4)))
print(function3())