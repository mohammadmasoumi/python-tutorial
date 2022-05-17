
def is_odd(a):
    # a: 12
    # you should return a bool
    return a % 2 == 1

new_list = []
for item in [12, 13, 14, 15]:
    # item: 12
    # True: is_odd(12)
    if is_odd(item):
        new_list.append(item)

print(list(filter(is_odd, [12, 13, 14, 15])))
print(new_list)