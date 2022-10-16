# Logical operator

# && ||  !
# and or not

# condition1 and condition2
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

a = 0
print(a != 0 and 12 // 0)
print(a and 12 // 0)
print(True and a) # False?(0)
print(a and True) # 0 

# b = True and a
# if True and a:

# ZeroDivisionError: integer division or modulo by zero
# print(a == 0 and 12 // 0)

# if a:

c = True
d = 1

print(id(c), id(d))

print("----------------------------")

a = 1
print(True or a) # True
print(a or True) # 1
print(True and a) # 1
print(False and 1) # False
print(a and True) # True 

a = 0
print(True or a) # True
print(a or True) # True
print(True and a) # 0
print(a and True) # 0

# 
print(True or 1 or 12)
print(12 or 1 or True)

# 
# if 12 or 1 or True:
