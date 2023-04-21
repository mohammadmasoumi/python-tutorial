# Count all decorated function's calls
import functools

def call_count(f):
    call_count.count = 0
    print("Called")

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        call_count.count += 1
        print(f"{f.__name__} called {call_count.count}")
        return f(*args, **kwargs)
    
    return wrapper


@call_count
def f1():
    pass

@call_count
def f2():
    pass

for _ in range(3):
    f1()
    f2()