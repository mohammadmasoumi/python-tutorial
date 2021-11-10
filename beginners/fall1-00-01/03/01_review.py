# int

an_int = 12

print(int(True))
print(int(False))

# ?
print("--------------------")
print(bool(True))
print(bool("Ali"))
print(bool(12))
print(bool(0))
print(bool(0.0))

# float
print(float(True))
print(float(False))

# operation
# int -> float
# bool -> int -> float

# float + int -> float + float(int)
# float + bool -> float + float(bool)
# int + bool -> int + int(bool)
print(type(12.2 + 12))
print(type(12.2 + 12.2))
print(type(True + 12.2))

# implicit casting
# b = float(True) + 12.2
b = True + 12.2
c = False + 12.2

print(b)
print(c)

# print(12 + "ali") Error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(12 + int("12"))
