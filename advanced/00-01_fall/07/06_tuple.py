a_list = ["a", "b"]
a_tuple = ("a", "b")
a_tuple_1 = ("a",)

print(len(a_list))
print(len(a_tuple))

a_tuple_2 = (1, "True", True, 1.0)
a_tuple_3 = (1, 1, "True", True, 1.0)

t1 = tuple((1, 2))
t2 = tuple((1, 2))

# immutable
# int
# str
# float
# bool
# tuple

# mutable
# list
# set
# dict


a1 = [1, 2]
# t3 = (1, 2)
t3 = (1, '2', False, 10.2, None)

# t3 = ([1, 2], [3, 4])
# t3 = (a1, [3, 4])
# t4 = (1, 2)

t4 = (1, '2', False, 10.2, None)
# t4 = ([1, 2], [3, 4])
# t4 = (a1, [3, 4])

# a1.append(3)

print(t3)
print(t4)

# print(id(t1))
# print(id(t2))
# 2447401053824
# 2447401053184
# 2994665338576
# 2994665338576

print(id(t3))
print(id(t4))
