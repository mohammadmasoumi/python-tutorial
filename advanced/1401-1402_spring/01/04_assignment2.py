
def call_me(f, *args):
    f(*args)


def printer_1(args):
    print(f"args1: {args}")
    
def printer_2(args):
    print(f"args2: {args}")
    

# printer_1("asghar")
call_me(f=printer_1, msg="asghar")

# printer_2("akbar")
call_me(printer_2, "akbar")