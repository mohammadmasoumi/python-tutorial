def my_decorator(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


# w = my_decorator(my_function)
# w: wrapper
# w()

@my_decorator
def sum1(a, b):
    return a + b


@my_decorator
def sum2(a, b, c):
    return a + b + c



# a = wraper(10, 20) 
a = sum1(10, 20)

print(a)