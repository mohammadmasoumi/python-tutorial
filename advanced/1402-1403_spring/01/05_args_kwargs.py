def c_add(numbers):
    s = 0
    for number in numbers:
        s += number

    return s

def python_add(*numbers):
    # packing
    # *numbers = 12, 13, 14, 15
    # numbers: (12, 13, 14, 15)
    # tuple
    s = 0
    for number in numbers:
        s += number

    return s


print(c_add([12, 13, 14, 15]))
print(python_add(12, 13, 14, 15))

# packing
a, b = 12, 13
print(a, b)
a, *b = 12, 13, 14
print(a, b)
*a, b = 12, 13, 14
print(a, b)
# for index, item in enumerate([12, 13, 14]):
#     print()

# for elem in enumerate([12, 13, 14]):
#     index, item = elem


def python_add(a, *numbers, b):
    # def python_add(a, b, *numbers):
    # packing
    # a, *numbers, b = 11, 12, 13, 14, 15, 16
    # *numbers = 12, 13, 14, 15
    # numbers: (12, 13, 14, 15)
    # tuple
    s = 0
    for number in numbers:
        s += number

    return s

print(python_add(11, 12, 13, 14, b=16))

# def python_add(a, *numbers, b):
#     s = 0
#     for number in numbers:
#         s += number

#     return s

# # Exception
# python_add(11, 16, 12, 13, 14, 15)


def python_add(a, b, *numbers):
    # packing
    # a, *numbers, b = 11, 12, 13, 14, 15, 16
    # *numbers = 12, 13, 14, 15
    # numbers: (12, 13, 14, 15)
    # tuple
    s = 0
    for number in numbers:
        s += number

    return s


print(python_add(11, 12, 13, 14))


def python_add(**numbers):
    # packing
    # **numbers = 11, 12, 13, 14, 15, 16
    # {"a": 11, "b": 12, "c": 13, "d": 14}
    s = 0
    for number in numbers.values():
        s += number
    return s


print(python_add(a=11, b=12, c=13, d=14))

def function(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, kwargs: {kwargs}")


funct, e=15)
# TypeError: functionion(10, 11, 12, 13, d=14() got multiple values for argument 'a'
# function(10, 11, 12, a=13, d=14, e=15)
# TypeError: function() got multiple values for argument 'a'
# function(10, 11, 12, d=14, e=15, a=13)
# function(10, a=11, 12, d=14, e=15, 13) # syntax error
# function(10, a=11, d=14, e=15, 13) # syntax error
# function(10, a=11, d=14, e=15)
function(10, b=11, d=14, e=15) 
