# params

def adder(a, b):
    # a = 12
    # b = 13
    return a + b

def adder2(a, b):
    # a = 12
    # b = 13
    # c = a, b
    # print(type(c))
    # multiple return with ,
    return a + b, abs(b - a)

# 
add = adder(120, 130)

print(adder(12, 13))
print(add)

print(adder2(12, 13))
add1, sub1 = adder2(12, 13)