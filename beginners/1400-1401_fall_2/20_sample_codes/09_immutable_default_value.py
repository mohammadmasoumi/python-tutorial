

def function_with_int_as_default_value(a=1000):
    print(f"a: {a}, id(a): {id(a)}")
    return a


function_with_int_as_default_value()
function_with_int_as_default_value()
print("--------------------------------")


def function_with_str_as_default_value(a="hello"):
    print(f"a: {a}, id(a): {id(a)}")
    return a


function_with_str_as_default_value()
function_with_str_as_default_value()
print("--------------------------------")


def function_with_float_as_default_value(a=1000.10):
    print(f"a: {a}, id(a): {id(a)}")
    return a


function_with_float_as_default_value()
function_with_float_as_default_value()
print("--------------------------------")



def function_with_bool_as_default_value(a=True):
    print(f"a: {a}, id(a): {id(a)}")
    return a


function_with_bool_as_default_value()
function_with_bool_as_default_value()
print("--------------------------------")
