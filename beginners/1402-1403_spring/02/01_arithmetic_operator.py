# 'A'
# "Ali"

# int: 12
# str: "Ali"
# float: 12.2
# bool: True/False
# list: [1, 2]

a = 'ali'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(12 + "ali")

# float + float = float
print(12.2 + 12.8)

# int + float = float
print(12 + 12.0)

# float div
print(11 / 5)

# true div
print(11 // 5)

# repeat string
a = "Ali" * 10
# "AliAliAliAliAliAliAliAli" + "\n"
# "Ali", "Ali", "Ali", "Ali", "Ali", "Ali", 
print("Ali" * 10)

print([1, 2] * 10)
print([[1, 2]] * 10)

# True => 1
# False => 0
# int + bool = int  
# bool + int = int
print(True + 1) # 2
print(1 + True) # 2
print(False + 1) # 1
print(1 + False) # 1

print(True * 10)
print(False * 10)

# ZeroDivisionError: division by zero
# print(True / False)

print(True ** 2)

print((True + True) * [1, 2])

# TypeError: can't multiply sequence by non-int of type 'float'
# print(2.2 * [1, 2])

# TypeError: can only concatenate str (not "bool") to str
# print("Ali" + True)

print(*[1, 2], sep=", ")

print(12 + 2 * 14)

# the same priority: LEFT TO RIGHT
# () ** * / + - 
print(12 + 2 * 14 * 2)