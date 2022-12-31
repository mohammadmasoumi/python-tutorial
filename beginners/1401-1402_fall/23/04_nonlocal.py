# a = 12

# def f1():
#     global a

#     a = 12
#     a += 1
#     print(a)

#     # SyntaxError: name 'a' is used prior to global declaration
#     # global a
#     # a += 1
#     # print(a)

#     b = a
#     b += 1
#     print(b)


# # global a 
# f1()
# print(a)

# global f2
a = 1

def f1():
    # nonlocal f2
    a = 10

    def f2():
        # local f2
        # a = 100

        # global a 
        # a += 1

        nonlocal a
        a += 1

        print(f"f2[a]: {a}")

    print(f"f1[a]: {a}")
    f2()
    print(f"f1[a]: {a}")

print(f"global[a]: {a}")
f1()
print(f"global[a]: {a}")
# NameError: name 'f2' is not defined. Did you mean: 'f1'?
# f2()