# anonymous function

"""
snake_case

def FUNC_NAME(inputs):
    # FUNCTION BODY
    pass
"""

def adder(a, b):
    return a + b

def multiply_by_2(a):
    return a *2

# function: variable
# variable:
#   name: adder
#   value: adder() ...
#   type: function


print(type(adder))

# anonymous
"""
EXPOSABLE
Once you use it
"""

my_list = [1, 2, 3, 4]

# <map object at 0x00000220D2109CF0>
print(map(lambda x: x*2, my_list))
# print(list(map(lambda x: x*2, my_list)))

# iterable
iterator = map(lambda x: x*2, my_list)
iterator = map(multiply_by_2, my_list)

#   iterable: you can't for loop over it
#   iterator: you can for loop over it

# list -> iter(list)
# iterable -> iterator

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # StopIteration
#
my_list = [1, 2, 3, 4]

for item in my_list:
    # 0, [1, 2, 3, 4]
    # 1, [2, 3, 4]
    # 2, [2, 4]
    my_list.remove(item)

print(my_list)  # [2, 4]


def my_for(l):
    iterator = iter(l)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

# WRONG
asghar = lambda x: x*2
print(asghar(2))

# INPUTs and OUTPUTs
# only one output
asghar = lambda x,y,z: x*y*z


