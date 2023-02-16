# range index
#          -6 -5 -4 -3 -2 -1
#          0  1  2  3  4  5
my_list = [1, 2, 3, 4, 5, 6]

"""
# single indice
my_list[2]

# slice 
end: not included
my_list[start: end: step]
"""

# range index
print(my_list[1:3:1])  # [2, 3]
print(my_list[1:5:2])  # [2, 4]
print(my_list[1:3:2])  # [2]
print(my_list[1:3:3])  # [2]
print(my_list[3:3:1])  # []

# my_list = [1, 2, 3, 4, 5, 6]
# default step: +1
print(my_list[1:3])  # [2, 3]
print(my_list[1:])  # [2, 3, 4, 5, 6]
print(my_list[:2])  # [1, 2]
print(my_list[:2:-1])  # [6, 5, 4]
print(my_list[:2:2])  # [1]
print(my_list[:2:-2])  # [6, 4]
print(my_list[2::-2])  # [3, 1

# my_list = [1, 2, 3, 4, 5, 6]
print(my_list[::-1])  # reverse: [6, 5, 4, 3, 2, 1
print(my_list[::-2])  # [6, 4, 2]
print(my_list[::])  # [1, 2, 3, 4, 5, 6]

# negative index
#            -6 -5 -4 -3 -2 -1
#            0  1  2  3  4  5
# my_list = [1, 2, 3, 4, 5, 6]
print(my_list[-1:-5:2])  # []
print(my_list[-1:5:2])  # []
print(my_list[-5:5:2])  # [2, 4]
print(my_list[-5:5:-1])  # []

print("--------------------------")
a = my_list[::-1]

print(id(a))
print(id(my_list))

# reversed: builtin function
# cast to list: list(item)
# int("12")
print(list(reversed(my_list)))

# TypeError: can't multiply sequence by non-int of type 'list'
# print([1, 2] * [3, 4])
