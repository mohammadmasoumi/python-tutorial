# non local variable


def function1():
    a, b, c = 10, 11, 12

    def function2():
        # search in nearest outer leyer
        # a, b, c = 100, 110, 120
        a, b, c = 100, 110, 120

        def function3():
            nonlocal a
            a += 1
            print(f"[function3] a: {a}, b: {b}, c: {c}")

        print(f"[before func3] a: {a}, b: {b}, c: {c}")
        function3()
        print(f"[after func3] a: {a}, b: {b}, c: {c}")

    print(f"[before func2] a: {a}, b: {b}, c: {c}")
    function2()
    print(f"[after func2] a: {a}, b: {b}, c: {c}")


function1()
