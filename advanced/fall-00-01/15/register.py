__REGISTRATION = {}


def register(func):
    def wrapper(*args, **kwargs):
        __REGISTRATION[func.__name__] = [func, args, kwargs]

        with open("spy.txt", "a") as file:
            args_name = ' | '.join(args)
            kwargs_name = ' | '.join([f"{k}:{v}" for k, v in kwargs.items()])
            text = f"[{func.__name__}]: args: {args_name}, kwargs: {kwargs_name}\n"
            file.write(text)

    return wrapper


def print_register():
    for func_name, func in __REGISTRATION.items():
        print(func_name, func[0](*func[1]))
