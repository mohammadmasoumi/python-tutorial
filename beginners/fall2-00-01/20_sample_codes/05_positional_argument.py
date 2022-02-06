# positional argument

def three_numbers_adder(x, y, z):
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    return x + y + z


print(three_numbers_adder(12, 13, 14))
print(three_numbers_adder(12, z=13, y=14))
print(three_numbers_adder(12, 13, z=14))
print(three_numbers_adder(z=12, y=13, x=14))

# Try these ones out
# TypeError: three_numbers_adder() got multiple values for argument 'x'
# print(three_numbers_adder(12, x=13, y=14))

# TypeError: three_numbers_adder() got multiple values for argument 'y'
# print(three_numbers_adder(12, 13, y=14))
