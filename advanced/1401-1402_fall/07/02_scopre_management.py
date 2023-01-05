# scope management

"""
global -> in the main body of file
local
non-local
"""
# global variable
a = 12

# def f1():
#     # local variable
#     # a = 13

#     # a = a + 1
#     # UnboundLocalError: local variable 'a' referenced before assignment
    
#     global a

#     a += 1
#     print(a)

#     def f2():
#         a = 100
#         print(a)

#     f2()

def f3():
    a = 15
    
    def f4():
        # a = 14
        # UnboundLocalError: local variable 'a' referenced before assignment
        # a += 1
        # a = a + 1

        # global a
        # a += 1

        nonlocal a
        a += 1

        print(a) # non-local

    f4()
    print(a) # local

"""
1. search in local scope
2. search in non-local
3. search in global scope
"""
print(a)
# f1()
# print(a)
f3()

    