# "12 13 14 15" - input()
# ['12', '13', '14', '15'] - input().split()
# [12, 13, 14, 15] - map(int, input().split()) 

w
# map(function, iterable)
# iterable: چیزی که روی آن میتونی بچرخی
# casting
# print(int("12"))

def cast_to_int(item):
    return int(item)

# n = list(map(int, input().split()))
# ['12', '13', '14', '15']
# 12 = cast_to_int('12')
# 13 = cast_to_int('13')
# 14 = cast_to_int('14')
# 15 = cast_to_int('15')
n = list(map(cast_to_int, input().split()))

# you can iterate over it
# obj map
# <map object at 0x0000014A55191988>

print(n)
print(list(n))

# for item in n:
#     print(item)