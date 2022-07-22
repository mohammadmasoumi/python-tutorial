# exception handling 


while True:
    try:
        # code block
        divider = int(input())
        print(12/divider)
        break
    except (ZeroDivisionError, ValueError) as e:
        if isinstance(e, ZeroDivisionError):
            print("Can't divide by zero! Give it another shot!")
        elif isinstance(e, ValueError):
            print("You must enter digits! Give it another shot!")

