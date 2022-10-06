sum([1, 2, 3])


# def
# a =  [1, 2]
# b =  [3, 4]
def add_two_list1(a, b):
    a.extend(b)
    return b


def add_two_list2(a, b):
    a.extend(b)
    return a


#      add_two_list ()
# print(    add_two_list(    [1, 2], [3, 4]       )        )
# print(              [1, 2, 3, 4]                         )

#                    a       b
print(add_two_list1([1, 2], [3, 4]))
print(add_two_list1([11, 12], [13, 14]))
print(add_two_list1([111, 112], [113, 114]))

print(add_two_list2([1, 2], [3, 4]))
print(add_two_list2([11, 12], [13, 14]))
print(add_two_list2([111, 112], [113, 114]))
