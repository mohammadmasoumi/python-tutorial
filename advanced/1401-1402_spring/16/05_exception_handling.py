try:
    # code block
    divider = int(input())
    res = 12/divider

except (ZeroDivisionError, ValueError) as e:
    if isinstance(e, ZeroDivisionError):
        print("Can't divide by zero! Give it another shot!")
    elif isinstance(e, ValueError):
        print("You must enter digits! Give it another shot!")

else:
    print(f"res: {res}")

finally:
    # code block
    print("I run anyway!")


# try:
#   connect to db
# except (ConnectExceptino) as e:
#   pass
# else:
#   query [2]
# finally:
#   close connection


# try:
#   connect to db
#   query [1]
# except (ConnectExceptino) as e:
#   pass
# finally:
#   close connection