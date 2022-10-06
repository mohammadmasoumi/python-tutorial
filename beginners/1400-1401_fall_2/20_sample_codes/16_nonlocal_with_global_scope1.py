
a, b, c = 1, 2, 3


def function1():
    a, b, c = 10, 20, 30

    print(
        f"[BEFORE-FUNC1] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")

    def function2():
        # Change a, b, c from global scope.
        global a, b, c
        a, b, c = 100, 200, 300

        print(
            f"[FUNC2] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")

    function2()
    print(
        f"[AFTER-FUNC1] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")


print(
    f"[BEFORE] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")
function1()
print(
    f"[AFTER] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")
