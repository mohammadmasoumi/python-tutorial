"""
name: a_tuple
value: (1, 2, 3)
id: id(a_tuple)
address
"""
# 140712621377552
# 140712621377552
a = 12
b = 12
print(id(a))
print(id(b))

# immutable
a_tuple1 = (1, 2, 3)
a_tuple2 = (1, 2, 3)

a_tuple3 = a_tuple1

# the same id
print(f"a_tuple1: {id(a_tuple1)}")
print(f"a_tuple1: {id(a_tuple2)}")
