a = 1

def f1():
    a = 10
    b = 20

    def f2():
        a = 100

        def f3():
            # a = 1000
            nonlocal a
            nonlocal b

            # a = a + 1
            a += 1

            print(f"f3[a]: {a} {b}")

        print(f"f2[a]: {a}")
        f3()
        print(f"f2[a]: {a}")

    print(f"f1[a]: {a}")
    f2()
    print(f"f1[a]: {a}")

print(f"global[a]: {a}")
f1()
print(f"global[a]: {a}")