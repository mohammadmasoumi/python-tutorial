
def my_decorator(f):
    # f: my_function
    def wrapper():
        # return f()
        return 10 + f()

    return wrapper


# w = my_decorator(my_function)
# w: wrapper
# w()

@my_decorator
def my_function():
    # return print("Hello")
    return 10

# a = wrapper()
a = my_function()
print(a)