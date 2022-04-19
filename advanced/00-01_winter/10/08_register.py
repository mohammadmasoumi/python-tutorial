PLUGINS = dict()

"""
PLUGINS = {
    'asghar': asghar,
    'akbar': akbar
}
"""
def register(func):

    def wrapper():
        func_name = func.__name__
        PLUGINS[func_name] = func
        return func()

    return wrapper


@register
def asghar():
    print("Hello I am asghar")
    return "asghar"

@register
def akbar():
    print("Hello I am akbar")
    return "akbar"


asghar()
akbar()

print(PLUGINS)

print("--------------------")
for func_name, func in PLUGINS.items():
    print(f"I am calling {func_name}: {func()}")