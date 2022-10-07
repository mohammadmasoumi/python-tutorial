# Arithmetic operator

"""
+
-
/
//
%
*
**
"""
# int = int + int
print(12 + 12)

# float = int + float
print(12 + 12.0)

# int = int + int(bool)
print(12 + True)

# float = float + float
print(12.3 + 13.7)
print(12.3 + 13.2)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(12 + '12')
# print(12 - '12')

print('a' * 12) # aaaaaaaaaaaa
print(12 * 'a')

# TypeError: can't multiply sequence by non-int of type 'float'
# print(12.0 * 'a')
# print(12.3 * 'a')
# print('a' ** 2) # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# TypeError: can't multiply sequence by non-int of type 'str'
# print('a' * 'a')
#  print('aaaaaaaaaaaa' / 12)

print(True * 12)
print(False * 12)

print(True * True)
print(True + True)
print(True / True)

# concatenation
print("ali" + "asghar")
print("ali" + " asghar")
print("ali" + " " + "asghar")
print("ali " + "asghar")

# TypeError: can't multiply sequence by non-int of type 'str'
# print('a' * 'b')
# print('' * 'b')

# TypeError: can only concatenate str (not "int") to str
# '' + 1000
# print('' * 12 + 1000)

a = [0] * 10
print(a)
a[0] += 1
print(a)

# [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print([1, 2] * 10)

# [[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], ...]
print([[1, 2] * 10] * 10)

# [[1, 2], 3, [1, 2], 3, [1, 2], 3, [1, 2], 3, [1, 2], 3]
print([[1, 2], 3] * 10)

# -----------------------------
#    Obj        Obj        Obj
# [[1, 2], 3, [1, 2], 3, [1, 2], 3, [1, 2], 3, [1, 2], 3]
a = [[1, 2], 3] * 10
a[0].append(4)
print(a)

# -----------------------------
b = [[1, 2] * 10] * 3
b[0].append(3)
print(b)