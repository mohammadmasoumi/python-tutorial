a_list = [1, 2, 3, 4]

for item in enumerate(a_list):
    # (0, 1) tuple
    idx, a = item
    print(idx, a, item, type(item))
