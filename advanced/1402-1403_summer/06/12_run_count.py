
def run_count(f):  # run once per decorated function
    count = 0

    def wrapper(*args, **kwargs):  # run whenever you run the decorated function
        nonlocal count
        count += 1

        print(f"{f.__name__} has called {count} times.")
        return f(*args, **kwargs)

    return wrapper


@run_count
def add(a, b):
    return a + b


add(10, 12)
add(10, 12)
add(10, 12)
