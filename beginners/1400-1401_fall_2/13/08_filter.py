# map
# filter(method, iterator)

my_list = [12, 13, 14, 15]


def just_odds(item):
    # return True False
    # return item % 2
    # return item % 2 != 0
    return item % 2

    # return None


print(list(filter(just_odds, my_list)))
