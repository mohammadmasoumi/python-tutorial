def say_greeting():
    """
    seek for return keyword?

    return None

    1. no return statement
    2. return 
    3. return None
    """
    # [4]
    print("Hello")
    # [5]

def invoker(func): # arguments: func
    # func = say_greeting
    # [2]
    print("Start ...")
    
    # res = None
    # [3][6]
    # say_greeting()
    res = func() # invoke

    # [7]
    print("End ...")

    # [8]
    return res


# TypeError: 'int' object is not callable
# invoker(12)
# TypeError: 'str' object is not callable
# invoker("hello")
#[1][9]
# a = None
a = invoker(func=say_greeting)
# [10] end