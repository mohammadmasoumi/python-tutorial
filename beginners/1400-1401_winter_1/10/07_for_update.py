my_list = [1, 2, 3, 4]

index = 0
for elem in my_list:
    elem += 2
    # my_list[0] = elem
    my_list[index] = elem
    index += 1

    # print(my_list)

print(my_list)

# immutable
# a = 12
# print(id(a))
# a = a + 2
# print(id(a))

# mutable
# a = [12]
# print(id(a))
# a.append(14)
# print(id(a))
