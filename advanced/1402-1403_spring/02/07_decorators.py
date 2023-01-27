# decorator without input
def decorated_f(function):
    # function: f1
    print(f"{function.__name__}")
    def wrapper():
        print(f"Before calling {function.__name__}")
        # res = function()
        print(f"After calling {function.__name__}")
        return 12

    return wrapper

@decorated_f
def f1():
    print("f1 has called!")

# @decorated_f
# def f2():
#     print("f2 has called!")

# wrapper = decorated_f(f)
# wrapper()
print(f1)
# a = f1()
# print(a)
# f2()
