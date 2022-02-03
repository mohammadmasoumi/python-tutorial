def call_me1():
    print("Hello")
    print("Call me 1")
    print("Bye")

def caller(f):
    # f = call_me1
    print("Hello")
    f()
    print(f()) # print( None = f() )
    print("Hello")
    print("Bye")

# print(      caller(      call_me1     )       ) # print(None = caller(      call_me1     ))
# TypeError: 'NoneType' object is not callable
# print(      caller(      call_me1()     )       )