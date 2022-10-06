

def remove_repetition(iterable):
    common = {}

    for item in iterable:
        common[item] = 1

    return list(common.keys()) 


print(remove_repetition([1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5]))