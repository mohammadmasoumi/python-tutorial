import time
import functools

def timer(func):

    @functools.wraps(func)
    def wrapper():
        s = time.perf_counter()
        func()
        e = time.perf_counter()
        print(f"consumed_time: {e - s}")

    return wrapper


@timer
def greeting():
    print("Hello How are you?")


greeting()

# what decorator do?
# wrapper = timer(greeting)
# wrapper()

# wrapper replaced by greeting
print(greeting.__name__)