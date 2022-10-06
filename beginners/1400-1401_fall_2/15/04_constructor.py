# tuple() => constructor
a_tuple1 = tuple((1, 2, 3, 4))
# a_tuple2 = tuple(1) # TypeError: 'int' object is not iterable
a_tuple3 = tuple([1])
a_tuple4 = tuple((1,))
# a_tuple5 = tuple(1, ) # TypeError: 'int' object is not iterable
# a_tuple6 = tuple((1)) # TypeError: 'int' object is not iterable
a_tuple7 = tuple([1] + [1])  # => tuple([1, 1])
# a_tuple7 = tuple([1] + [1])

# ["ali", "asghar", "hassan", "akbar"]
print(["ali", "asghar"] + ["hassan", "akbar"])
# print(["ali", "asghar"] - ["hassan", "akbar"])
# print(["ali", "asghar"] * ["hassan", "akbar"])
# print(["ali", "asghar"] / ["hassan", "akbar"])
print(["ali", "asghar"] * 2)

print(a_tuple1)
print(a_tuple3)
print(a_tuple4)
# print(a_tuple5)
# print(a_tuple6)
print(a_tuple7)
print(type(a_tuple1))
# print(type(a_tuple2))
