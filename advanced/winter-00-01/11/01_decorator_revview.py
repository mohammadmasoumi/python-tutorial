
def run_twice(func):
    # func: greeting
    # func()
    # Hello
    # func() ?
    print("I'm calling ... ")
    
    # func()
    def wrapper():
        # print("Asghar")
        func()

    # wrapper()
    print("End of calling ...")

    return wrapper

def greeting():
    print("Hello")


# func: wrapper
# wrapper()
# Asghar
func = run_twice(greeting)
func()