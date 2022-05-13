# decorator
def run_twice(func):
    def wrapper():
        print("before call ...")
        func()
        func()
        print("after call ...")

    return wrapper

@run_twice
def say_greeting():
    print("Hello How are you?")

# f = wrapper
# f = run_twice(say_greeting)
# f()

say_greeting()