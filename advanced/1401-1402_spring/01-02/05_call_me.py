
def printer1(msg):
    print(f"[msg1]: {msg}")


def printer2(msg):
    print(f"[msg2]: {msg}")


def caller(f, param):
    # f: printer1, param: "Hello from the otherside" 
    # printer1( "Hello from the otherside" )

    # f: printer2, param: "Hello from the outside" 
    # printer2( "Hello from the outside" )
    f(param)


caller(printer1, "Hello from the otherside") # [*]
caller(printer2, "Hello from the outside")


