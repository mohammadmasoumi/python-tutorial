# non local variable


def function1():
    a, b, c = 10, 11, 12

    def function2():
        # read
        # a = a + 1
        # UnboundLocalError: local variable 'a' referenced before assignment
        # a += 1
        nonlocal a
        a += 1
        print(f"[function2] a: {a}, b: {b}, c: {c}")

    print(f"[before func2] a: {a}, b: {b}, c: {c}")
    # side effect => change a 
    function2()
    print(f"[after func2] a: {a}, b: {b}, c: {c}")


function1()
