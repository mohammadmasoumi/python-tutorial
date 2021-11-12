def test1(a):
    # multiple return keyword
    if a > 10:
        return

    print(a)

    return a


def test2(a):
    # single return
    # if a <= 10:
    if not (a > 10):
        print(a)
        return a
