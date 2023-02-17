# cast list

print(list("hello"))
# ["h", "e", "l", "l", "o"]

print("hello"[0])
print("hello"[-1])

for char in "hello":
    print(char)

print("-----------------------")
# print(list(123))

# TypeError: 'int' object is not iterable
# print(123[0])
# TypeError: 'int' object is not iterable
# [1, 2, 3]
# [123]
# ["1", "2", "3"]
# exception

# 3 TypeError: 'bool' object is not iterable
# print(list(True))

# TypeError: 'float' object is not iterable
# print(list(12.2))

print(list([1, 2, 3]))

# 2D WRONG
# exception WRONG
# [1, 2, 3]

my_list1 = [1, 2, 3]
my_list2 = list(my_list1)
# constructor
# list([1, 2, 3]) => create new list

print("---------------------")
print(my_list1 == my_list2)  # equal
print(my_list1 is my_list2)  # not equal

a = 12
b = int(a)
print("---------------------")
print(a == b)  # True
# print(id(a) == id(b))
print(a is b)  # True
