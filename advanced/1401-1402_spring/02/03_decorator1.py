# decorator
def run_twice(func):
    def wrapper(*args, **kwargs):
        # args: tuple, ("asghar", )
        # kwargs: {"name": "asghar"}
        print(args, kwargs)
        print("before call ...")
        # args: ("asghar", )
        # *args: "asghar"
        # func("asghar")
        # args: ()
        # if []:
        #     pass
        if args and args[0] == "ali":
            func(args, **kwargs)
            func(*args, **kwargs)

        print("after call ...")

    return wrapper

@run_twice
def say_greeting(name):
    """This a function"""
    print(f"Hello How are you? {name}")

say_greeting("asghar")
print("-----------------------")
say_greeting("ali")
print("-----------------------")
# IndexError: tuple index out of range
say_greeting()
# TypeError: say_greeting() got multiple values for argument 'name'
# say_greeting("akbar", 20, name="asghar", last_name="hamidi", age=12)

# -----------
# def say_greeting(name):
#     """This a function"""
#     print(f"Hello How are you? {name}")
# print(help(say_greeting))