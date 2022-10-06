# non local & global variable
a, b, c = 0, 1, 2


def function1():
    a, b, c, d = 10, 11, 12, 2000

    def function2():
        # search in nearest outer leyer
        # a, b, c = 100, 110, 120
        a, b, c = 100, 110, 120

        def function3():
            global a
            nonlocal b, d
            # nonlocal d
            a += 1
            b +=1
            d += 1
            print(f"[function3] a: {a}, b: {b}, c: {c}, d: {d}")

        print(f"[before func3] a: {a}, b: {b}, c: {c}")
        function3()
        print(f"[after func3] a: {a}, b: {b}, c: {c}")

    print(f"[before func2] a: {a}, b: {b}, c: {c}")
    function2()
    print(f"[after func2] a: {a}, b: {b}, c: {c}")


function1()
