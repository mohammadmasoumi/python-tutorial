# exception handling 


while True:
    try:
        # code block
        divider = int(input())
        print(12/divider)
        break
    
    except ZeroDivisionError:
        # exception handling
        print("Can't divide by zero! Give it another shot!")
    except ValueError:
        # exception handling
        print("You must enter digits! Give it another shot!")

