
#          0  1  2  3
my_list = [1, 2, 3, 10]

# acc = my_list.pop(0)
# for elem in my_list:
#     acc /= elem
# print(acc)

# my_list[::2]: [1, 3]
# for elem in my_list[::2]:
#     print(elem)

# index = 0
# for elem in my_list:
#     # index: 0, elem: 1
#     # index: 0, elem: 2
#     if index % 2 == 1:
#         print(elem)

#     index += 1

for elem in my_list:
    # if my_list.index(elem) % 2 == 1:
    
    # if 1: # bool(1)
    #   print("Hello")
    # my_list.index(elem) % 2 => [0, 1]
    # if 1: # bool(1)
    #   print("Hello")
    # if 0: # bool(0)
    #   print("Hello")
    # if "": # bool("")
    #   print("Hello")

    if my_list.index(elem) % 2:
        print(elem)

    if not my_list.index(elem) % 2:
        print(elem)
        