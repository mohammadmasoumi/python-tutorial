# function

"""
def [METHODNAME](PARAMS)|:
    FUNCTION BODY

def add(x, y): # x, y : params
    # x: 10, y: 12
    # x: 20, y: 22
    return x + y

# args(value) => params(variable)

# 10, 12 arguments
c = add(10, 12) # c: 22
d = add(20, 22) # d: 42


FINAL_RES: map(FUNCTION, MY_LIST)
MY_LIST: [1, 2, 3, 4]
FINAL_RES: [FUNCTION(1), FUNCTION(2), FUNCTION(3), FUNCTION(4)]

"""


def add(x, y):
    return x + y


def asghar(x, y):
    return x + y


c = add(10, 12)
d = asghar(10, 12)

print(c)
print(d)
print(type(add))
print(add)

# anonymous function
# lambda params: outputs
print(lambda x, y, z: x+y+z)
print(lambda x, y: x+y)  # add

# map update
my_list = [1, 2, 3, 4]

print([item*2 for item in my_list])


def multi(x):
    # x: 1
    return x * 2


my_list = [1, 2, 3, 4]
new_my_list = []

# new_my_list: []
for item in my_list:
    # item: 1, multi(1) => 2, new_my_list: [2]
    # item: 2, multi(2) => 4, new_my_list: [2, 4]
    res = multi(item)
    new_my_list.append(res)

print(list(map(lambda x: x*2, my_list)))
print(list(map(multi, my_list)))
print(map(multi, my_list))

"""
f(x) = x^2

# x:1 x^2 => 1
f(1) = 1
# x: 2  x^2 => 4
f(2) = 4
"""

# filter

"""
map => update
filter => filter

if lambda x: x % 2 == 0 return True => you have that item in the final list
"""

my_list = [1, 2, 3, 4]

# update
print([item*2 for item in my_list])
print(list(map(lambda x: x*2, my_list)))

# filter
print([item for item in my_list if item % 2 == 0])
print(list(filter(lambda x: x % 2 == 0, my_list)))


my_list = [1, 2, 3, 4]

print([item*2 for item in my_list if item % 2])
print(map(lambda x: x*2, filter(lambda x: x % 2, my_list)))
