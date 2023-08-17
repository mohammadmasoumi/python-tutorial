# reusable

# a: 10, b: 11, c: 12
# a: 20, b: 21, c: 22
def complicated_formula(a, b, c): 
    x = a + b + c
    y = a + x + c
    z = a + y + 10
    m = 10 * (z + y) ** 2

    return m


# 10, 11, 12
a = 10
b = 11
c = 12
# x = a + b + c
# y = a + x + c
# z = a + y + 10
# m = 10 * (z + y) ** 2 ** 3
complicated_formula(a, b, c)
complicated_formula(10, 11, 12) # call, invoke

# 20, 21, 22
a = 20
b = 21
c = 22
# x = a + b + c
# y = a + x + c
# z = a + y + 10
# m = 10 * (z + y) ** 2 ** 3
complicated_formula(20, 21, 22) # call, invoke

# 30, 31, 32, ....