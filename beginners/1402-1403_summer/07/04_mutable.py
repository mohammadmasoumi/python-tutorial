a = [1, 2, 3]
b = [1, 2, 3]

print(f"a: {id(a)}, b: {id(b)}")
print(a == b) # check value
print(a is b) # check instance, check id
print("------------")
print(id(a[0]), id(b[0]))
