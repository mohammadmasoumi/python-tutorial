# positional args
def add(*args,**kwargs):
    print(f"args: {args}, kwargs: {kwargs}")


# print(sum(add(10: 12)))
# TypeError: add() takes 0 positional arguments but 2 were given
add(10, 12)
add(10, a=12)
add(10, a=12, b=13)
add(a=12, b=13)
# add(a=12, b=13, 14) Exception
