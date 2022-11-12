def logger_decorator(f):
    # f: greeting
    def wrapper(*args: tuple, **kwargs: dict):
        #                        map(   function, iterable )
        # iterable2 = all elements in args have been stringify
        args_str = ",".join(map(lambda x: str(x), args))
        kwargs_str = ",".join(
            [f"{key}: {value}\n" for key, value in kwargs.items()])
        print(f"Start {f.__name__}, args: {args_str} | kwrags: \n{kwargs_str}")
        res = f(*args, **kwargs)
        print(f"End {f.__name__}, args: {args} | kwrags: {kwargs}")

        return res

    return wrapper


@logger_decorator
def greeting(name):
    print(f"Hello, How are you? {name}")
    return name


@logger_decorator
def chineese_greeting(name, gender):
    print(
        f"Hello, How are you? {'Mr.' if gender == 'male' else 'Miss/Mrs.'}{name}")
    return name


# wrapper = logger_decorator(greeting)
# name = wrapper(name)
# name = greeting("Asghar")
# print(name)

# print(chineese_greeting('Asghar', 'female'))
# print(chineese_greeting(name='Asghar', gender='female'))
print(chineese_greeting(name='Asghar', gender='female'))

name = "Asghar"
print("Hello, How are you name")
print(f"Hello, How are you {name}")
