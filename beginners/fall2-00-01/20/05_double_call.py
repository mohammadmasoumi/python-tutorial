# first class object

def func():
    print("Bye")

def func3():
    return func

def func1(func):
    # func = func2
    return func3

def func2():
    print("Hello")

func1(func2)()()
# func3()()
# func()

# TypeError: 'NoneType' object is not callable
# func1(func2)()()
# func2()()
# None()
