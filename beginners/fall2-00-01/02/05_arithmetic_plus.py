# arithmetic operator
# implicit casting

print(f"12 + True = {12 + True}")  # int + bool = int
# print(f"12 + int(True) = {12 + int(True)}")

print(f"12 + 1.0 = {12 + 1.0}")  # int + float = float
# print(f"float(12) + 1.0 = {float(12) + 1.0}")  # int + float = float

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(f"23 + '12' = {23 + '12'}")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(f"23 + '12' = {23 + 'a'}")


# string concatenation
a = "ali"
print(f"{a + ' ' + a}")
print(f"{a + '' + a}")
print(f"'ali' + ' hossein' = {'     ali ' + ' hossein'}")
print(f"'ali' + ' ' + 'hossein' = {'ali' + ' ' + 'hossein'}")
print(f"'ali' + 'hossein' 'hello' = {'ali' + ' hossein' + 'hello'}")

# bool + bool
print(f"True + True = {True + True}")
print(f"True + False = {True + False}")
print(f"False + False = {False + False}")

# ZeroDivisionError: division by zero
# print(f"False / False = {False / False}")
# print(12 / 0)

print(f"True + 12.9 = {True + 12.9}")
