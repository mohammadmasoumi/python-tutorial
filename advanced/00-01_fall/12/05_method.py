global_var = 100
c = 200


def func1():
    a = 10

    def func2():
        b = 20
        # c = 400

        # global scope

        # global c
        # local scope
        c = 40

        def func3():
            # global c = 30
            print(f"Good Job, {global_var}, a: {a}, b: {b}, c: {c}")

        # func3()
        print(f"Nice Job {global_var}, a: {a}, b: {b}, c: {c} ")
        return func3

    print(f"Bad Job global_var: {global_var}, a: {a}, c: {c} ")
    # func2()
    return func2


# func1func2func3()
func1()()()
# func2()
print(f"c: {c}")
