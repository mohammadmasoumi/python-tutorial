
def call_me(f, msg):
    # f: printer_1
    # msg: "asghar"
    # printer_1("asghar")
    f(msg)


def printer_1(msg):
    print(f"msg1: {msg}")
    
def printer_2(msg):
    print(f"msg2: {msg}")
    

# printer_1("asghar")
call_me(f=printer_1, msg="asghar")

# printer_2("akbar")
call_me(printer_2, "akbar")