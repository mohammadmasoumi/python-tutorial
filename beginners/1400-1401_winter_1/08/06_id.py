# int - id
a1 = 12
b1 = 12
# -oo +oo cache
print(f"id(a1): {id(a1)}, id(b1): {id(b1)}")

a2 = 100000000
b2 = 100000000
print(f"id(a2): {id(a2)}, id(b2): {id(b2)}")
print("------------------------------------")

# str - id
c1 = "hello"
c2 = "hello"
print(f"id(c1): {id(c1)}, id(c2): {id(c2)}")

# float - id 
d1 = 100000000.1
d2 = 100000000.1
print(f"id(d1): {id(d1)}, id(d2): {id(d2)}")
print("------------------------------------")


# list - id
e1 = [1, 2, 3, 4]
e2 = [1, 2, 3, 4]
print(f"id(e1): {id(e1)}, id(e2): {id(e2)}")
