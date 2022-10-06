# 1
numbers = input().split()  # default space

# my_list = [1, 2, 3]
# my_list[2] = 4

# ['1', '2', '3', '4', '5']
# [1, 2, 3, 4, 5]

# final answer
# variable
# index = 0
counter = 0
for number in numbers:
    # index 0
    # numbers[index] = int(number)
    # numbers[counter] = int(number)
    numbers[numbers.index(number)] = int(number)
    # index += 1
    counter += 1

print(numbers)

# # --------------------------------------  WRONG
# # if we do not increase index
# index = 0
# for number in numbers:
#     # index 0
#
#     numbers[index] = int(number)
#     # index += 1
#
# print(numbers)
#
# # --------------------------------------  WRONG
# # if we increase index and then update list
# index = 0
# for number in numbers:
#     # index 0
#     try:
#         index += 1
#         numbers[index] = int(number)
#     except:
#         pass
#
# print(numbers)
