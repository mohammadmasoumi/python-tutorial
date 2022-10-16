# default value

def add(a, b, c, d=10):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    return a + b + c + d


print(add(10, 11, 12))
print(add(10, 11, 12, 13))


def my_sort(iterable, reverse=False):
    pass


my_sort([3, 2, 4, 1])
my_sort([3, 2, 4, 1], reverse=True)