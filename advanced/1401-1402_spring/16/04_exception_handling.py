try:
    # code block
    divider = int(input())
    res = 12/divider
    # raise ZeroDivisionError()
except (ZeroDivisionError, ValueError) as e:
    if isinstance(e, ZeroDivisionError):
        print("Can't divide by zero! Give it another shot!")
    elif isinstance(e, ValueError):
        print("You must enter digits! Give it another shot!")
else:
    print(f"res: {res}")


try:
    # code block
    divider = int(input())
    res = 12/divider
except (ZeroDivisionError, ValueError) as e:
    if isinstance(e, ZeroDivisionError):
        print("Can't divide by zero! Give it another shot!")
    elif isinstance(e, ValueError):
        print("You must enter digits! Give it another shot!")


print(f"res: {res}")