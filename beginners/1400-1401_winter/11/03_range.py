# range builtin function


# range index
# index[start, end, step]

# range(start, end, step)

# end: 10
a = range(10)
# range(0, 10)
print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(a))

# for item in range(10):
#     print(item)

b = range(100)
print(b)
# print(list(range(100)))
print(list(b))

# for item in b:
#     print(item)

print("----------------------")
# TypeError: 'bool' object is not iterable
# for item in not range(10, 100, 2):
#   print(item)

a = not range(10, 100, 2)
# a = not 2 | a = False
# TypeError: 'bool' object is not iterable
# print(type(a))
# print(list(a))

# for item in range(10, 100, 2):
#     print(item)


# def test1(a, b ,c):
#     return 2

# def test2(a, b ,c):
#     # code block
#     return a + b + c

# def test3():
#     return 10, 20

# test2(10, 20 ,30)
# test2(10, 40 ,50)