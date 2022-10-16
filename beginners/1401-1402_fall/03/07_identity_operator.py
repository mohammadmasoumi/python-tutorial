# identity Operator
# Same object

# is VS ==

a = 12
b = 12

print(a is b)
print("-----------")

a = [12, 13]
b = [12, 13]

# print(id(a) == id(b))
print(a is b)
print(a is not b)
print(a == b)
print(id(a), id(b))
print("-----------")

a =  [12, 13]
b = a
print(a is b)
print(id(a), id(b))
print("-----------")


