# int
a_string = "12"
print(12)
print(int(12))
print(int('12'))
# ValueError: invalid literal for int() with base 10: 'ali'
# a3 = int(a_string)
print(int(True))
print(int(False))
print(int(12.0))
# a4 = int("ali")

# implicitly casting
# float + bool -> float + float(bool)
print(12.2 + True)
print(True + 12.2)

# float + int -> float + float(int)
print(12.2 + 12)

print("-----------------------------------")
# str
print(str(True))
print(str(12))
print(str(12.2))

# bool
print("-----------------------------------")
# "" -> false, 0 -> False
print(bool(""))
print(bool("ali"))
print(bool("a"))
print(bool(12))
print(bool(-12))
print(bool(0))
print(bool(0.0))

# ZeroDivisionError: float division by zero
# print(0.0/0.0)
print(bool(str(int("12"))))
