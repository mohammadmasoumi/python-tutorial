"""
def handler(btn_name, value):
    pass

tkinter

Button(callback=handler("btn1", 2))
Button(callback=handler)
"""
def handler(*args, **kwargs):
    print(f"Handled, args: {args}, kwargs: {kwargs}")

def partial_function(f, *args, **kwargs):
    # args: ("asghar", 22), kwargs: {}

    # partial():
    def partial(*fargs, **fkwargs):
        # args: ("asghar", 22)
        # fargs: ("hamid", 23)
        # f("asghar", 22, "hamid", 23)
        return f(*args, *fargs, **{**kwargs, **fkwargs})

    return partial

# my_partial: func
# partial_function(handler, name="asghar", age=22)
my_partial = partial_function(handler, "asghar", 22)
# my_partial()
# my_partial(name="hamid", age=23)
my_partial("hamid", 23)


# my_partial = lambda : handler("asghar", 22)