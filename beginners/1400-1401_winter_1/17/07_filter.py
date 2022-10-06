# filter
# n = int(input())

def is_even(item):
    # باید یک مقدار بولین برگردانید
    if item % 2 == 1:
        return False
    # else:
        # return True
    return True

# print(is_even(n))
# print(is_even( int(input() )))

my_list = [1, 2, 3, 4]

# filter(function, iterable)
# is_even(1) False
# is_even(2) True
# is_even(3) False
# is_even(4) True
# [2, 4]
print(list(filter( is_even, my_list )))

