# global scope
# global variables
a = 12
c = 14
d = 15

def my_func():
    # c
    global c, d
    b = 10 # local scope
    # use a in global scope
    # new local scope a 
    # new variable
    # local scope
    a = 13
    c += 1 # you want to change a global variable
    # you must use global keyword
    print(f"a: {a}, b: {b}, c: {c}")


print(f"a: {a}, c: {c}")
my_func()
print(f"a: {a}, c: {c}")

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(b)