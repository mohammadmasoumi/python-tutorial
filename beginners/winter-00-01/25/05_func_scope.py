a = 12
h = a

# pass value by reference
def add(c, b):
    # c = a  
    print(f"c: {c}, id(c): {id(c)}")
    return c + b

print(f"a: {a}, id(a): {id(a)}")
print(f"a: {h}, id(a): {id(h)}")
# print(id(add))

print(add(a, 12))
print(a)