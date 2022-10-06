def my_decorator(f):
    def wrapper(a, b):
        # a: 10, b: 20
        # f: sum
        # sum(10 + 10, 20 + 10)
        # res = sum(20, 30)
        # res: 50
        # return res
        return f(a + 10, b + 10)

    return wrapper


# w = my_decorator(my_function)
# w: wrapper
# w()

@my_decorator
def sum(a, b):
    # return print("Hello")
    return a + b

# a = wraper(10, 20) 
a = sum(10, 20)

print(a)