n = int(input())


# the largest width of pattern
pattern_width  = (2 * n) - 1 

def get_star_count(row):
    star_count = (2 * row) + 1
    return star_count


for idx in range(n):
    print(("*" * get_star_count(idx)).center(pattern_width))

for idx in range(n-2, -1, -1):
    print(("*" * get_star_count(idx)).center(pattern_width))

