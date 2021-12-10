a = [-50, 51, 1, 2, 49]


def mix(item):
    return abs(50 - item)


a.sort(key=mix, reverse=True)
print(a)
