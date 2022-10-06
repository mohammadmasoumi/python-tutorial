# functional programming


def make_multiplier_of(x):
    # x binds to the function

    def multiplier(n):
        return n * x

    return multiplier


times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(f"times3(10): {times3(10)}")
print(f"times3(11): {times3(11)}")
print(f"times3(12): {times3(12)}")

print(f"times5(10): {times5(10)}")
print(f"times5(11): {times5(11)}")
print(f"times5(12): {times5(12)}")


#
def func1(param1):
    def func2(param2):
        return param1 * param2

    return func2


def func1_alternative(param1, param2):
    return param1 * param2


print(func1(10)(12))
