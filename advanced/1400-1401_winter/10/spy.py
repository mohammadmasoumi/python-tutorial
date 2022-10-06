import requests

def logger(func):
    
    def wrapper(*args, **kwargs):
        # greeting("Ali")
        # args: ("Ali", )
        # greeting(name="Ali")
        # kwargs: {"name": "Ali"}

        args_repr = " | ".join(args)
        kwargs_repr =  " | ".join([f"{key}:{value}" for key, value in kwargs.items()])
        result = func(*args, **kwargs)

        with open("spy.txt", "a") as file:
            file.write(f"[{func.__name__}]: args: {args_repr}, kwargs: {kwargs_repr}, result: {result}\n")
        
        # requests.post(url)

    return wrapper