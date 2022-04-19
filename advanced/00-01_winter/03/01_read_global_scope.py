
# global, nonlocal
a, b, c = 10, 11, 12


def func_name():
    # a, b, c = 1, 2 , 3
    print(a, b, c)


print(a, b, c)
func_name()