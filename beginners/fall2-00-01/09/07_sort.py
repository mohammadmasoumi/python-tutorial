a = [-50, 51, 1, 2, 49]


def mix(item):
    return abs(50 - item)


def my_sort(key):
    # key: function

    for item in a:
        key(item)
        # a.index(item)


a.sort(key=mix, reverse=True)
print(a)
