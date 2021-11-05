# global -> change in module level
# nonlocal -> change in function scope

local_to_module = 10


# local_to_func = 30
# local_to_func = 30

def nonlocal_func():
    local_to_func = 20

    def nonlocal_func1():
        # local changes
        # no module level
        # just inside function
        nonlocal local_to_func  # read and write
        # # local_to_func = 20
        local_to_func += 20

        def nonlocal_func2():
            nonlocal local_to_func
            local_to_func += 20
            print(f"[inside-inside] local_to_func: {local_to_func}")

        nonlocal_func2()
        print(f"[inside] local_to_func: {local_to_func}")

    nonlocal_func1()
    print(f"[outside] local_to_func: {local_to_func}")


# local_to_func = 20


def global_func():
    local_to_func = 20

    # global local_to_module
    def global_func1():
        # NameError: name 'local_to_func' is not defined
        global local_to_module
        # local_to_func = 20
        local_to_module += 20
        # local_to_func += 20
        print(f"[inside] local_to_func: {local_to_module, local_to_func}")

    global_func1()
    # print(f"[outside] local_to_func: {local_to_module, local_to_func}")


nonlocal_func()
print("-------------------------------")
global_func()
