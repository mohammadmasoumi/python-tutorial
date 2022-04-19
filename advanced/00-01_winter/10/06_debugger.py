# https://mybrowseraddon.com/dark-mode.html?v=0.4.2&type=install

def debugger(func):

    def wrapper(*args, **kwargs):
        # greeting("Ali")
        # args: ("Ali", )
        # greeting(name="Ali")
        # kwargs: {"name": "Ali"}

        args_repr = " | ".join(args)
        kwargs_repr =  " | ".join([f"{key}:{value}" for key, value in kwargs.items()])
        result = func(*args, **kwargs)
        print(f"[{func.__name__}]: args: {args_repr}, kwargs: {kwargs_repr}, result: {result}")

    return wrapper


@debugger
def greeting(name, last_name):
    print(f"Hello, {name} - {last_name}")
    # return None


a = greeting(name="Aliakbar", last_name="mohajer") # key: value
print("---------------")
greeting("Aliakbar", "mohajer") # positional arguement