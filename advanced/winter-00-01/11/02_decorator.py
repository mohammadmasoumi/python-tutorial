
def run_twice(func):
    # func: greeting
    def wrapper():
        print("Before")
        func()
        func()
        func()
        print("After")

    return wrapper

@run_twice
def greeting():
    print("Hello")


greeting()

# func = run_twice(greeting)
# func: wrapper
# func() == wrapper()
