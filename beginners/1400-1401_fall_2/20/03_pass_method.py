def call_me1():
    print("Call me 1")

def call_me2():
    print("Call me 2")

def caller():
    # func = call_me
    # yell = shout
    # yell()
    # a()
    pass

def caller2(a):
    # a = call_me1
    # a()
    # call_me1()
    a()

print(      caller2(      call_me1     )       )
print(      caller2(      call_me2     )       )

# TypeError: caller() takes 0 positional arguments but 1 was given
# caller(call_me1)

# print(      caller(call_me1)       )
