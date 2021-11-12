# pass argument to wrapper

# 2
def run_twice(func):
    # *args, **kwargs
    def wrapper(*args, **kwargs):
        # before
        print("before")

        print(f"args: {args}, kwargs: {kwargs}")

        func(*args, **kwargs)
        func(*args, **kwargs)

        # after
        print("after")

    return wrapper


# @ decorator
@run_twice
def greeting(name, age, address=""):
    print(f"Hello, How are you Mr/Mrs {name}. I am {age} years old")
    # print(f"Hello, How are you Mr/Mrs {name if True else 'asghar'}. I am {age} years old")


greeting(name="Ali", age=26)
greeting("Ali", 26)
