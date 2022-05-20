# filter
# "12 13 14 15"
# n = ["12", "13", "14", "15"]
# map(int, n) => [12, 13, 14 ,15]
n = input().split()

def is_even(item):
    if item % 2 == 1:
        return False
    return True


print(list(filter( is_even, map(int, n) )))

