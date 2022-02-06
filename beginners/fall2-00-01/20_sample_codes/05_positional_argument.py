# positional argument

def adder(x, y, z):
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    return x + y + z


print(adder(12, 13, 14))
print(adder(12, z=13, y=14))
print(adder(12, 13, z=14))
print(adder(z=12, y=13, x=14))

# Try these ones out
# TypeError: adder() got multiple values for argument 'x'
# print(adder(12, x=13, y=14))

# TypeError: adder() got multiple values for argument 'y'
# print(adder(12, 13, y=14))
