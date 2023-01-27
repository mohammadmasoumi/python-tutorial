# int
# str
# function

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a * b

def call_me(f):
    # f: add
    print("Before calling f")
    print(f(12, 13))
    print("After calling f")

def call_me2(f, a, b):
    # f: add
    print("Before calling f")
    for i in range(10):
        print(f(a, b))
    print("After calling f")


call_me(add)
call_me2(add, 12, 13)