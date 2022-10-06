
def function1():
    a, b, c = 1, 2, 3

    print(
        f"[BEFORE-FUNC1] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")

    def function2():
        # read nonlocal variables from outer scope
        print(
            f"[FUNC2] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")

    function2()
    print(
        f"[AFTER-FUNC1] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")


function1()
