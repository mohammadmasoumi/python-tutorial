# pass argument to wrapper
# 4
def run_multiple(times):
    def run_multiple(func):
        # *args, **kwargs
        def wrapper(*args, **kwargs):
            # before
            print("before")

            for _ in range(times):
                func(*args, **kwargs)

            # after
            print("after")

        return wrapper

    return run_multiple


# @ decorator
@run_multiple(10)
def greeting(name, age):
    print(f"Hello, How are you Mr/Mrs {name}. I am {age} years old")
    # print(f"Hello, How are you Mr/Mrs {name if True else 'asghar'}. I am {age} years old")


greeting(name="Ali", age=26)
# greeting("Ali", 26)
