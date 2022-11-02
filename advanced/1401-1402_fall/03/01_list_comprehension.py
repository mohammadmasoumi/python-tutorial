# list Comprehension
my_list = [1, 2, 3, 4]
even_my_list = []

for item in my_list:
    if item % 2 == 0:
        even_my_list.append(item)

print(even_my_list)

# list Comprehension
print("---------------------------")
print([item * 2 for item in my_list])
#     [[result in final list]  for [item] in [list]  [condition] ]
print([item for item in my_list if item % 2 == 0])
print([item for item in my_list if item % 2])
# --------------------------
print([item * 2 if item % 2 else item // 2 for item in my_list])
# [2, 1, 6, 2]

# --------------------------
# 2D list
my_list = [[1, 2], [3, 4]]

# flatten list
# my_list = [1, 2, 3, 4]
# items: [1, 2] item: 1, 2
# items: [3, 4] item: 3, 4

print([item for items in my_list for item in items])
print([item * 2 for items in my_list for item in items])
print([item * 2 for items in my_list for item in items if item % 2])
print([item * 2 if item % 2 else item // 2 for items in my_list for item in items])

# inline if
c = 12

# if c % 2 == 0:
if int(input()) % 2 == 0:
    b = "Hello"
else:
    b = "Bye"

# b = "Hello" if c % 2 == 0 else "Bye"
b = "Hello" if int(input()) % 2 == 0 else "Bye"
print("Hello" if int(input()) % 2 == 0 else "Bye")

# comparison operator
# == != > < <= >=

# falsey values:
# bool(falsey value) ===> False

# int
# bool(0) => False
# bool(-120) => True
# bool(3) => True
# bool(4) => True

# flaot
# bool(0.0) => False
# bool(-120.2) => True
# bool(3.7) => True
# bool(4.1) => True

# str
# bool("") => False
# bool("    ") => True
# bool("1") => True
# bool("*") => True

# list
# bool([]) => False
# bool([1]) => True

# falsey and truthy
# bool(item % 2)
# item: 3
# item % 2 => 1 bool(1) => True
# Odd
if item % 2:
    print("Hello")
