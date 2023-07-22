# decorator

"""
decorator

 - logging
 - cache
 - timer
 - RAM usage
 - disable
 - deprecate
 - run twice
 - run many times | decorator with inputs
 - sandwich
 - italic/strong
 - ...

 - is_authenticated
 - routing
 - ...

"""


def decorator_name(f):
    # f: decorated function
    print("decorated function")

    def wrapper(*args, **kwargs):
        # before executing function
        res = f(*args, **kwargs)
        # after executing function 

        # res decorated function
        return res

    return wrapper

# run once 
# wrapper = decorator_name(f)
# add() -> wrapper()
# add() -> wrapper()

@decorator_name
def add(a, b):
    return a + b

print("before calling")
add(10, 12)
add(10, 12)
print("after calling")