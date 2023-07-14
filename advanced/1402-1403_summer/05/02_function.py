# functions are first class objects
# Object


def add(a, b):
    return a + b

def dummy():
    print("Dummy")

# def call_me(f, a, b):
#     # f: dummy
#     print(f"Calling {f.__name__}")
#     res = f(a, b)
#     print(f"{f.__name__} called!")
#     return res
    

a = int(input())
b = int(input())

# call_me(dummy)
# print(call_me(add, a, b))

print(f"Calling {dummy.__name__}")
dummy()
print(f"{dummy.__name__} called!")

print(f"Calling {add.__name__}")
add(a, b)
print(f"{add.__name__} called!")

print(f"Calling {add.__name__}")
add(10, 20)
print(f"{add.__name__} called!")

print(f"Calling {dummy.__name__}")
dummy()
print(f"{dummy.__name__} called!")