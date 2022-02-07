# non local variable


def function1():
    a, b, c = 10, 11, 12

    def function2():
        # nonlocal a 
        a = 12
        # SyntaxError: name 'a' is assigned to before nonlocal declaration
        # nonlocal a
        print(f"[func2] a: {a}, b: {b}, c: {c}")

    print(f"[before func2] a: {a}, b: {b}, c: {c}")
    function2()
    print(f"[after func2] a: {a}, b: {b}, c: {c}")


function1()
