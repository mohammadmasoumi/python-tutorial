# 1
# numbers = input().split('*')

# # update list item
# my_list = [1, 2, 3]
# my_list[2] = 4

numbers = input().split()  # default space

# 1
print(numbers)
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# print(int(numbers))

# ['1', '2', '3', '4', '5']
# [1, '2', '3', '4', '5']
# 1
# index = 0

for number in numbers:
    # number 1
    # number 2

    numbers = int(number)

    # print(number, type(number))
    # numbers = int(number)  # int('5')
    # print(f"numbers: {numbers}")

    print(numbers)

print(numbers)