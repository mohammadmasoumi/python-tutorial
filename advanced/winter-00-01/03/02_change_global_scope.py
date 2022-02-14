
# global, nonlocal
# هر چیزی که داخل بدنه فایل باشد میشود global 
a, b, c = 10, 11, 12


def func_name():
    global a, b, c

    a += 1 
    b += 2
    c += 3

    print("inside", a, b, c)


print("before", a, b, c)

func_name()

print("after", a, b, c)

