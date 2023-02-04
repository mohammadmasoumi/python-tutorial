def decorator(n):
    def do_twice(f):
        def wrapper(*args, **kwargs):
            nonlocal n
            
            while n > 0:
                n -= 1
                f(*args, **kwargs)
            # for _ in range(n):
        return wrapper

    return do_twice

@decorator(10)
def f():
    print("Hello")

f()

# w = do_twice(f)
# w()

# w = do_twice(10)
# w(f)