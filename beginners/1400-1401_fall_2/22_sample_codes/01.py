
def sum_avg(iterable):
    s = sum(iterable)
    return s, s / len(iterable)

print(sum_avg([1, 2, 3, 4]))