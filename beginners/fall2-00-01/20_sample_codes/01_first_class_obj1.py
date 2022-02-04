# functions are first class object in python


def square(x):
    """Square of x."""
    return x*x


def cube(x):
    """Cube of x."""
    return x*x*x


# create a dictionary of functions
x = 5
funcs = {
    'square': square,
    'cube': cube,
}


for key, method in funcs.items():
    # call functions with x = 5
    print(f"Calling {key} with {x}: {method(x)}")
