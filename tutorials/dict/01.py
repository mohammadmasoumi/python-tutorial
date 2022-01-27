d = {"d": 1,"a": 5, "b": 3, "c": 4}

def reverse(item):
    return item[1]

print(d.items())
print(dict(sorted(d.items(), key=reverse)))