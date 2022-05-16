def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


num = 10
num = operate(inc, num)
print(f"num: {num}")
num = operate(inc, num)
print(f"num: {num}")
