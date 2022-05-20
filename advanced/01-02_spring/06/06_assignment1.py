def decorator(f):

    def wrapper(*args, **kwargs):
        # print(f"args: {args}, kwargs: {kwargs}")
        print("before execution")
        # say_greeting(name="Asghar")
        res = f(*args, **kwargs)
        print("after execution")
        return res

    return wrapper


@decorator
def say_greeting(name):
    print(f"Hello, {name}")
    # 1. 
    # 2. return
    # 3. return None

# output = wrapper("Asghar")
output = say_greeting(name="Asghar")
print(output)