# return none
# output: 1 or OO

def return_none1():
    pass


def return_none2():
    return


def return_none3():
    return None


def return_none4():
    print("Hello")
    a = 10


print(return_none1())
print(return_none2())
print(return_none3())
print(return_none4())

print("-------------------")
"""
Terminal
Hello
None
None

print("hello") -> None
print(None) -> None
print(None) -> None

print(print(    print("hello")   ))
print(print(         None        ))
print(               None         )
None
"""
print(print(print("hello")))
