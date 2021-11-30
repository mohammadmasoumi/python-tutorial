a = 12
b = 13

a, b = b, a

# curly braces
print(f"a: {a}")
print(f"b: {b}")
# print(f"c: {c}") # NameError: name 'c' is not defined

# ___________________________________________

c = 12
d = 13

d = c + d
c = d - c
d = d - c
