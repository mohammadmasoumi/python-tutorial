# Force developer to pass arguments by their key and valueu


def adder1(*, x, y, z):
    return x + y + z


def adder2(x, *, y, z):
    return x + y + z


def adder3(x, y, *, z):
    return x + y + z


# ------------------ adder1 ------------------
print(adder1(x=11, y=12, z=13))
print(adder1(x=11, z=13, y=12))
print(adder1(y=12, x=11, z=13))
print(adder1(y=12, z=13, x=11))
print(adder1(z=13, x=11, y=12))
print(adder1(z=13, y=12, x=11))

# Try these ones out
# print(adder1(11, y=12, z=13))
# print(adder1(11, 12, z=13))
# print(adder1(11, 12, 13))

# ------------------ adder2 ------------------
print(adder2(11, y=12, z=13))
print(adder2(11, z=13, y=12))

# Try these ones out
# print(adder2(11, 12, z=13))
# print(adder2(11, 12, 13))

# ------------------ adder3 ------------------
print(adder3(11, 12, z=13))

# Try these ones out
# print(adder3(11, 12, 13))
