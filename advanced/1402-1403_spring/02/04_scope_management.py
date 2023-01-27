# READ a
# 1. local a
# 2. nonlocal
# 3. global
a = 1

def f1():
    # Exception
    # print(f"[f1]: Before a: {a}")
    # a = 10
    # print(f"[f1]: After a: {a}")
    a = 10

    def f2():
        # nonlocal a
        a = 100

        def f3():
            nonlocal a
            a = 1000
            print(f"[f3]: a: {a}")

        print(f"[f2]: Before a: {a}")
        f3()
        print(f"[f2]: After a: {a}")

    print(f"[f1]: Before a: {a}")
    f2()
    print(f"[f1]: After a: {a}")

print(f"[Main]: Before a: {a}")
f1()
print(f"[Main]: After a: {a}")
