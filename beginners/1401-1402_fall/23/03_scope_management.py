# scope: global 
a = 1

"""
Read

1. search for local variable
2. search for non-local variable
2. search for global variable

"""
def f1():
    # local
    # a = 10

    # print(a)

    # 1. define a local variable called "a"
    # 2. read the value of "a"
    # a = a + 1
    # UnboundLocalError: local variable 'a' referenced before assignment
    # a += 1
    # print(a)
    # return None

    # a = 10
    # a += 1
    # print(a)

    global a
    a += 1
    print(a)


print(a)
f1()
print(a)
# res = f1()
# print(res)
# print(f1())