# decorator

def decorator(f):
    # function inside function
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    
    return wrapper

# wrapper = decorator(function)
# wrapper("ali")
@decorator
def function(name):
    print(f"Hello {name}")



