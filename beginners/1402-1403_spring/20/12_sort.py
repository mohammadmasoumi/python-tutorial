d = {
    'k1': 'v11',
    'k2': 'v22',
    'k3': 'v01',
    'k4': 'v32',
}


def sort_by_value_num(item):
    # item: (key, value)
    # item: tuple
    key, value = item

    # return -int(value[1:])
    return int(value[1:])


"""
sorted
                         keyword key=asghar, reverse=True
(__iterable: iterable, *, key: None = ..., reverse: bool = ...)
"""
# [(key, value), (key, value), (key, value)]
print(dict(sorted(d.items(), key=sort_by_value_num)))
print(dict(sorted(d.items(), key=sort_by_value_num, reverse=True)))

# for item in d.items():
#     sort_by_value_num(item)
