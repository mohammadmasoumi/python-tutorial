# filter
def is_even(item):
    if item % 2 == 1:
        return False
    return True

my_list = [1, 2, 3, 4, 5, 6]

print(my_list[:2] + list(filter( is_even, my_list[2:] )))

