operator = 0

# module level
# local_variable_to_func = 200


def func():
    # non-local readonly
    # global operator
    global operator
    operator += 1
    # local variable
    # operator = 2
    local_variable_to_func = 100
    print(f"[inside] operator: {operator}")

    def func1():
        # non local variable read-only
        # local_variable_to_func += 10

        # solution 1
        # global local_variable_to_func
        # Pycharm warning -  Global variable 'local_variable_to_func' is undefined at the module level
        global operator, local_variable_to_func

        # print(local_variable_to_func + 10)
        local_variable_to_func += 1

        # if declare local_variable_to_func in func
        # and declare local_variable_to_func in module level
        # local_variable_to_func searches in module
        print(f"local_variable_to_func: {local_variable_to_func}")

        operator += 100

    return func1()
    # operator += 1


print(f"[outside] operator: {operator}")
func()
print(f"[outside] operator: {operator}")
