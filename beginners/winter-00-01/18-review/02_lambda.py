# lambda function

"""
f(x) = x ^ 2
g(x) = x ^ 3
f(x, y) = x ^ 2 + y ^ 2

function structure:
 - name
 - inputs
 - outputs

def function_name(inputs):
    return outputs

def add(a, b):
    # a: 12, b: 13
    # a + b: 25
    #  code block
    c = a + b 
    return c
    # return a + b

def add_and_multiple_by_2(a, b, c):
    d = a + b + c
    d *= 2
    return d


# a, b  ---> f ---> a + b
# positional argument
result1 = add(12, 13)
result1 = 25
result2 = add(120, 130)

res1 = add_and_multiple_by_2(10, 11, 12)
print(res1)

# چندتا ورودی میتونی داشته باشی
# یک دونه بیشتر خروجی نمیده
function_name = lambda inputs: output

lambda a, b, c, d: a + b + c + d
lambda : 10

usage:
    - map
    - filter

"""

def add(a, b):
    return a + b

# anonymous
add = lambda a, b: a + b
print(add(12, 13))


def add_and_multiple_by_2(a, b, c):
    d = a + b + c
    d *= 2
    return d

# 
add_and_multiple_by_2(10, 11, 12)
res1 = add_and_multiple_by_2(10, 11, 12) 
print(add_and_multiple_by_2(10, 11, 12))
print(res1)

