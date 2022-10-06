def call_me(f):
    # takes function as variable
    # f = printer_1
    # yell = shout
    # printer("asghar")
    print("----------- BEFORE CALL -----------")
    f("asghar")
    print("----------- AFTER CALL -----------")
    

def printer_1(msg):
    print(f"msg1: {msg}")
    
def printer_2(msg):
    print(f"msg2: {msg}")
    

call_me(printer_1)
call_me(printer_2)