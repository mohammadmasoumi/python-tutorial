a_tuple = (12, 13, 14)
a_tuple3 = (0, )
a_tuple2 = ("12", "13", "14")

# TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
# print(int(a_tuple))
# print(float(a_tuple))

# TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
# print(int(a_tuple2))

# false
# bool([])
# bool(())
# bool({})
# bool("")
# bool(0)

print(str(a_tuple))
print(list(a_tuple))
print(tuple(a_tuple))
print(set(a_tuple))
print(bool(a_tuple))
print(bool(a_tuple3))
print(bool(()))
