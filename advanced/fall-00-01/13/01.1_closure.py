# closures

def print_msg(msg):
    def printer():
        print(f"mes is : {msg}")

    # printer()
    return printer


# bind a variable into a function
other_func = print_msg("Hello")
other_func()
other_func()
other_func()
other_func()
other_func()

# del print_msg
other_func()
another = print_msg("Hello from other side!")
print("----------------------------------------")

another()
other_func()
del print_msg

another()
other_func()
