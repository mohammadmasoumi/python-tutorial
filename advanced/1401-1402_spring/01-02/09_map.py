
def cast_to_int(a):
    # a: '12'
    return int(a)


# n = list(map(int, input().split()))
# ['12', '13', '14', '15']
# 12 = cast_to_int('12')
# 13 = cast_to_int('13')
# 14 = cast_to_int('14')
# 15 = cast_to_int('15')
#               function              iterable

# new_list = []
# for item in ['12', '13', '14', '15']:
#     # item: '12'
#     # 12: cast_to_int('12')
#     new_list.append(cast_to_int(item))

print(list(map(cast_to_int, ['12', '13', '14', '15'])))