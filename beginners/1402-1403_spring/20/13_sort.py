d = {
    'k1': 51,
    'k2': 49,
    'k3': -1,
    'k4': 100,
    'k5': 25,
}


def sort_function(item):
    # item: (key, value)
    key, value = item
    return abs(50 - value)


print(dict(sorted(d.items(), key=sort_function)))
print(dict(sorted(d.items(), key=lambda item: abs(50-item[1]))))
